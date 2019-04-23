# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonLinesItemExporter

class QcwyjobPipeline(object):
    def __init__(self):
        self.path = open("qcwy.json","wb+")
        self.exporter = JsonLinesItemExporter(self.path,ensure_ascii=False)
        # self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        # self.exporter.finish_exporting()
        self.path.close()