import scrapy

class NurSpider(scrapy.Spider):
    name = "nur"
    start_urls = [
        "https://www.nur.kz/society/",
    ]

    def parse(self, response):
        for nur in response.css("li.block-infinite__item"):
            yield {
                "date": nur.css("time.preview-info-item-secondary::attr(datetime)").get()
            }

class NurSpiderGetContent(scrapy.Spider):
    name = "nurgetcontent"
    start_urls = [
        "https://www.nur.kz/society/2097218-pochti-na-dve-nedeli-perekroyut-odnu-iz-ulic-astany-iz-za-remonta/",
    ]

    def parse(self, response):
        for nur in response.css("div.formatted-body__content--wrapper"):
            yield {
                "content": nur.css("div.formatted-body__content--wrapper").get()
            }

class NurSpiderGetTitle(scrapy.Spider):
    name = "nurgettitle"
    start_urls = [
        "https://www.nur.kz/society/",
    ]

    def parse(self, response):
        for nur in response.css("li.block-infinite__item"):
            yield {
                "title": nur.css("a.js-article-link::text").get()
            }

class NurSpiderGetLink(scrapy.Spider):
    name = "nurgetlink"
    start_urls = [
        "https://www.nur.kz/society/",
    ]

    def parse(self, response):
        for nur in response.css("li.block-infinite__item"):
            yield {
                "link": nur.css("a.js-article-link::attr(href)").get()
            }