import scrapy

class DmozSpider(scrapy.Spider):
    name = "company"
    allowed_domains = ["imprensaoficial.com.br"]
    start_urls = [
        "http://balancos.imprensaoficial.com.br/Condiario.asp"
    ]

    def parse(self, response):
        

    def parse_companies(self, response):
        urls = response.xpath('//a')
        print(urls)
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
            # f.write(response.body)