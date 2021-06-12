import scrapy
from ..items import InsiderItem
from unidecode import unidecode

class InsiderHtmlSpider(scrapy.Spider):

    #Internsting list for insider.in website
    collection_name = 'Interesting_Events_insider'
    name = 'insider_html'
    allowed_domains = ['insider.in']
    start_urls = ['https://insider.in/all-digital-events-in-online']

    def parse(self, response):
        try:
            all=response.xpath("//div[@class='card-list-wrapper card-grid time-wrapper']/div/ul/li")
        except:
            all=[]

        pre='https://insider.in'
        i=1
        for element in all:
            url=element.xpath(".//div[@class='event-card ']/a/@href").get()
            request=scrapy.Request(pre+url,self.parse_url)
            yield request
            i+=1
            if(i>10):
                break

    def parse_url(self,response):

        event_item=InsiderItem()
        try:
            event_item['Headline']=unidecode(response.xpath("//h1[@class=' css-1izdngw']/text()").get())
        except:
            event_item['Headline']=""

        try:
            event_item['Genre']=unidecode(response.xpath("//p[@class='css-hc3kyf']/text()").get())
        except:
            event_item['Genre']=''

        try:
            dates_mode = response.xpath("//p[@class='css-8hlgow']/text()").extract()
            event_item['Dates'], event_item['Mode'] = unidecode(dates_mode[0]), unidecode(dates_mode[1])
        except:
            event_item['Dates'], event_item['Mode']='',''

        try:
            age_lang = response.xpath("//p[@class='css-1oqavfg']/text()").extract()
            event_item['Age'], event_item['Language'] = unidecode(age_lang[0]), unidecode(age_lang[1])
        except:
            event_item['Age'], event_item['Language']='25+','English'

        try:
            event_item['Price'] =unidecode("₹ "+response.xpath("//p[@class='css-q525hq']/text()").get())
        except:
            event_item['Price']='Free'

        print(event_item)
        yield event_item




