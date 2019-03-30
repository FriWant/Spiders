import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban_spider"
    start_urls = ['https://movie.douban.com/top250/',
                              ]

    custom_setting = {
                'FEED_EXPORT_ENCODING': 'utf-8',
            }

    def start_requests(self):
        header = {'User-Agent': "Mozilla\/5.0 (X11; Linux x86_64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/73.0.3683.86 Safari\/537.36"}
        yield scrapy.Request(url = self.start_urls[0], headers = header)


    def parse(self, response):

        for item in response.css('div.item'):
            
            
            yield {

                    'Title': item.css('span.title::text').get(),
                    'inq': item.css('span.inq::text').get(),
                    }
       
            NEXT_PAGE_SELECTOR = 'span.next a ::attr(href)'
            next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            if next_page:
                yield start_requests(
                        response.urljoin(next_page),
                        callback=self.parse,
                        )
