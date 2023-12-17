import scrapy


class FirstspiderSpider(scrapy.Spider):
    name = "firstspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            relative_url = book.css('li.next a::attr(href)').get()

            if 'catalogue/' in relative_url:
                book_url = "http://books.toscrape.com/" + relative_url
            else:
                book_url = "http://books.toscrape.com/catalogue/" + relative_url
            yield response.follow(book_url, callback= self.parse_book_page)

        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            if 'catalogue/' in next_page:
                next_page_url = "http://books.toscrape.com/" + next_page
            else:
                next_page_url = "http://books.toscrape.com/catalogue/" + next_page
            yield response.follow(next_page_url, callback= self.parse)

    def parse_book_page(self, response):
        pass