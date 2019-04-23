# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re
from qcwyjob.items import QcwyjobItem
class QcwyDemoSpider(CrawlSpider):
    name = 'qcwy_demo'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,java,2,1.html']

    rules = (
        Rule(LinkExtractor(allow=r'.+list/000000,000000,0000,00,9,99,java,2,\d+\.html'), follow=True),
        Rule(LinkExtractor(allow=r'.+[0-9]{9}\.html.+'), callback="parse_item",follow=True),
    )

    def parse_item(self, response):
        # 公司名称
        firmName = response.xpath("//div[@class='tBorderTop_box']/div[1]/a/p/text()").get()
        # 所属行业
        trade = response.xpath("//div[@class='com_tag']/p[3]/a[1]/text()").get()
        # 公司规模
        firmScale = response.xpath("//div[@class='com_tag']/p[2]/text()").get()
        # 工作地点
        workAddress = response.xpath("//div[@class='cn']/p[2]/text()").getall()[0].replace("\xa0", "").replace("\t","").replace("\r\n", "")
        # 公司地址
        firmAddress = response.xpath("//div[@class='bmsg inbox']/p/text()").getall()[1].replace("\t","")
        # 发布时间
        pub_time = response.xpath("//div[@class='cn']/p[2]/text()").getall()[4].replace("\xa0", "").replace("发布","").replace("\t", "")
        # 工资情况
        salary = response.xpath("//div[@class='cn']/strong/text()").get()
        # 学历要求
        edu = response.xpath("//div[@class='cn']/p[2]/text()").getall()[2].replace("\xa0", "")
        # 经验要求
        workexper = response.xpath("//div[@class='cn']/p[2]/text()").getall()[1].replace("\xa0", "")
        # 职位名称
        workName = response.xpath("//div[@class='cn']/h1/text()").get().replace("\t", "").replace("\r\n", "")

        # 职位信息
        context = "".join(response.xpath("//div[@class='bmsg job_msg inbox']//text()").getall()).replace("\r\n","").replace("\t","").replace("\\","//").replace(" ","")
        if re.findall("任职资格：|岗位要求：|任职要求|职位要求", context) != []:
            # 岗位职责
            workdesc = re.split("任职资格|岗位要求|任职要求|职业发展|职位要求",context)[0]
            # 任职资格
            workstatus = "任职资格：" + re.split("任职资格|岗位要求|任职要求|职业发展|职位要求", context)[1]
        else:
            workdesc = context
            workstatus = ""

        item = QcwyjobItem(firmName=firmName,trade=trade,firmScale=firmScale,workAddress=workAddress,firmAddress=firmAddress,pub_time=pub_time,salary=salary,edu=edu,
                           workexper=workexper,workName=workName,workdesc=workdesc,workstatus=workstatus)
        return item
