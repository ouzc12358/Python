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
    article_links = [link['href'] for link in links if link['href'].endswith('.html')]
    return ["http://paulgraham.com/" + link for link in article_links]

def fetch_and_save_article(url):
    article_content = fetch_page(url)
    if article_content:
        title, content = parse_article(article_content)
        if title and content:
            save_to_word(content, title)

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

def save_to_word(article_content, title):
    file_name = title.replace(" ", "_") + ".docx"
    file_path = os.path.join('articles', file_name)

    if not os.path.exists(file_path):
        doc = Document()
        doc.add_heading(title, 0)
        doc.add_paragraph(article_content)
        doc.save(file_path)
        logging.info(f"Saved '{title}' to Word document.")
    else:
        logging.warning(f"File '{file_name}' already exists. Skipping.")

def main():
    os.makedirs('articles', exist_ok=True)
    main_page_url = "http://paulgraham.com/articles.html"
    main_page_content = fetch_page(main_page_url)

    if main_page_content:
        article_links = parse_main_page(main_page_content)

        with ThreadPoolExecutor(max_workers=10) as executor:
            executor.map(fetch_and_save_article, article_links)

if __name__ == "__main__":
    main()
