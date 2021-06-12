import scrapy
from ..items import InsiderItem
from unidecode import unidecode

class NaadSpider(scrapy.Spider):

    #interesting urls from both sites
    collection_name = 'interesting_urls'
    name = 'i_list'
    start_urls = ['https://www.naadyogacouncil.com/en/events/']
    l=['insider','naad']

    def parse(self, response):
        # event_url=InsiderItem()
        for i in self.l:
            if (i == 'insider'):
                url='https://insider.in/all-digital-events-in-online'
                request = scrapy.Request(url, self.parse_url)
                yield request
            else:
                url='https://www.naadyogacouncil.com/en/events/'
                request = scrapy.Request(url, self.parse_url)
                yield request

    def parse_url(self,response):
        event_url=InsiderItem()
        if(response.url=='https://insider.in/all-digital-events-in-online'):
            try:
                all = response.xpath("//div[@class='card-list-wrapper card-grid time-wrapper']/div/ul/li")
            except:
                all=[]

            pre = 'https://insider.in'
            i = 1
            urls=[]
            for element in all:
                url = element.xpath(".//div[@class='event-card ']/a/@href").get()
                urls.append(pre+url)
                i += 1
                if (i > 10):
                    break

            event_url['Interesting_url']=urls
            yield event_url

        else:
            urls = []
            try:
                all = response.xpath("//div[@class='tribe-events-event-image']")
            except:
                all=[]

            for element in all:
                url = element.xpath(".//a/@href").get()
                urls.append(url)

            event_url['Interesting_url'] = urls
            yield event_url




