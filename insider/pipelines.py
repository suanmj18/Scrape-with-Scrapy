# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo

class InsiderPipeline:

    collection_name = 'Interesting_Events_TB1'
    def __init__(self):
        self.conn=pymongo.MongoClient(
            'localhost',
            27017
        )

        db = self.conn['Events'] #Name of Database
        # self.connection = db['Interesting_Events_insider']
        # self.connection = db['Interesting_Events_naadyyoga']
        # self.connection = db['interesting_urls']
        # self.connection = db['Not_interesting_urls']
        self.connection = db['Events_Tb']

    def process_item(self, item, spider):
        if hasattr(spider, 'collection_name'):
            self.collection_name = spider.collection_name

        value = dict(item)
        res={}

        if(self.collection_name=='Interesting_Events_insider'):
            res = {'Headline': value['Headline']}
        elif(self.collection_name=='Interesting_Events_naadyyoga'):
            res = {'Dates': value['Dates']}
        elif(self.collection_name=='interesting_urls'):
            res={'Interesting_url':value['Interesting_url']}
        elif(self.collection_name=='Not_interesting_urls'):
            res={'Not_Interesting_url':value['Not_Interesting_url']}

        self.connection[self.collection_name].update(res,dict(item),upsert=True)
        return item

