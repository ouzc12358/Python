import requests
from bs4 import BeautifulSoup
from docx import Document
import os
import logging
from concurrent.futures import ThreadPoolExecutor

# Set up basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logging.error(f"Error fetching {url}: {e}")
        return None

def parse_main_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    links = soup.find_all('a')
    article_links = [link['href'] for link in links if 'html' in link['href']]
    return ["http://paulgraham.com/" + link for link in article_links if not link.startswith("http")]

def fetch_and_parse_article(url):
    article_content = fetch_page(url)
    if article_content:
        title, content = parse_article(article_content)
        return title, content
    return None, None

def parse_article(content):
    try:
        soup = BeautifulSoup(content, 'html.parser')
        title = soup.find('title').text
        paragraphs = soup.find_all('p')
        article_content = "\n".join(paragraph.text for paragraph in paragraphs)
        return title, article_content
    except Exception as e:
        logging.error(f"Error parsing article: {e}")
        return None, None

def append_to_word(doc, article_content, title):
    doc.add_heading(title, level=1)
    doc.add_paragraph(article_content)
    doc.add_page_break()

def main():
    os.makedirs('articles', exist_ok=True)
    main_page_url = "http://paulgraham.com/articles.html"
    main_page_content = fetch_page(main_page_url)

    if main_page_content:
        article_links = parse_main_page(main_page_content)
        doc = Document()

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(fetch_and_parse_article, article_links)

            for title, content in results:
                if title and content:
                    append_to_word(doc, content, title)

        doc.save(os.path.join('articles', 'all_articles.docx'))
        logging.info("All articles saved to one Word document.")

if __name__ == "__main__":
    main()