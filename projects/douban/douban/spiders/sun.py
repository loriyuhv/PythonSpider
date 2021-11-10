import scrapy
from scrapy import Request
from urllib.parse import urlencode


class SunSpider(scrapy.Spider):
    name = 'sun'    # 爬虫名称
    MAX_PAGE = 10   # 最大爬取页数

    def start_requests(self):
        # 基础url地址
        base_url = "https://wz.sun0769.com/political/index/politicsNewest?"

        # 通过循环，构造10页的请求request
        for page in range(1, self.MAX_PAGE+1):
            data = {
                "id": "1",
                "page": page
            }
            params = urlencode(data)
            url = base_url + params     # 完整的url由 基础的url + 参数拼接而成
            # print(url)    # 查看构造的url
            yield Request(url, self.parse)

    def parse(self, response, **kwargs):
        # 解析页面
        banks = response.xpath('//div[@class="width-12"]/ul/li[@class="clear"]')
        item = {}
        for bank in banks:
            # 获取编号
            item["number"] = bank.xpath('./span[@class="state1"]/text()').extract_first().strip()
            # 获取状态
            item["status"] = bank.xpath('./span[@class="state2"]/text()').extract_first().strip()
            # 获取问政标题
            item["title"] = bank.xpath('./span[@class="state3"]/a/text()').extract_first().strip()
            # 获取响应时间
            item["resp_time"] = bank.xpath('./span[@class="state4"]/text()').extract_first().strip()
            # 获取问政时间
            item["req_time"] = bank.xpath('./span[@class="state5 "]/text()').extract_first()
            # 获取详细信息链接
            item["link"] = "https://wz.sun0769.com" + bank.xpath('./span[@class="state3"]/a/@href').extract_first().strip()
            # 传入管道，item类型是dict
            yield item

