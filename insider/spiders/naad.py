import scrapy
from ..items import InsiderItem
from unidecode import unidecode

class NaadSpider(scrapy.Spider):

    # Internsting list for naadyogacouncil.com website
    collection_name = 'Interesting_Events_naadyyoga'
    name = 'naad'
    allowed_domains = ['naadyogacouncil.com']
    start_urls = ['https://www.naadyogacouncil.com/en/events/']

    def parse(self, response):
        try:
            all=response.xpath("//div[@class='tribe-events-event-image']")
        except:
            all=[]

        for element in all:
            url=element.xpath(".//a/@href").get()
            request=scrapy.Request(url,self.parse_url)
            yield request

    def parse_url(self,response):

        event_item = InsiderItem()
        try:
            event_item['Headline'] = unidecode(response.xpath("//div[@class='wpv-grid grid-1-1  first unextended']/p[1]/b/text()").get())
        except:
            event_item['Headline'] = ""

        try:
            event_item['Genre'] = 'Yoga'
            event_item['Age'] = 'Family'
        except:
            event_item['Genre'] = ''
            event_item['Age'] = ''

        try:
            event_item['Dates'] = unidecode(response.xpath("//div[@class='day']/text()").get() + " " + response.xpath("//div[@class='month']/text()").get())
        except:
            event_item['Dates'] =''

        try:
            event_item['Language'] = unidecode(response.xpath("//div[@class='wpv-grid grid-1-1  first unextended']/p[4]/text()").get())

        except:
            event_item['Language'] = ''

        try:
            event_item['Price'] = unidecode(response.xpath("//div[@class='wpv-grid grid-1-1  first unextended']/p[5]/text()").get())
        except:
            event_item['Price'] = ''

        try:
            event_item['Mode'] = unidecode(response.xpath("//div[@class='wpv-grid grid-1-1  first unextended']/p[3]/text()").get())
        except:
            event_item['Mode'] = ''

        print(event_item)
        yield event_item