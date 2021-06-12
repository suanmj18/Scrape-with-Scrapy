from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

process.crawl('insider_html')
process.crawl('i_list')
process.crawl('naad')
