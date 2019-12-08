# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser


class ConfigurxSpider(scrapy.Spider):
    name = 'configurX'
    allowed_domains = ['https://configurx.it.abb.com/configurx/']
    start_urls = ['https://configurx.it.abb.com/configurx/content/Login.aspx']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            
            formdata={
                'txtLogin':' Thomas-tao.wang@cn.abb.com',
                'txtPassword':' System02',
                'cmdLogin':' Login'
            },
            callback=self.after_login
        )
    def after_login(self, response):
           if "Welcome" in response.body:
                self.logger.warning("Success")
                return   
