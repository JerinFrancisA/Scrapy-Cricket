# -*- coding: utf-8 -*-
import scrapy
from ..items import CricketItem


class CricspySpider(scrapy.Spider):
    name = 'cricspy'
    start_urls = [
        'https://sportstar.thehindu.com/cricket/icc-cricket-world-cup/icc-cricket-world-cup-2019-india-team-player-profiles-stats-virat-kohli-hardik-pandya-bumrah-dhoni-rohit/article27197602.ece',
        'https://sportstar.thehindu.com/cricket/icc-cricket-world-cup/icc-cricket-world-cup-2019-south-africa-team-player-profiles-stats-du-plessis-de-kock-steyn-rabada/article27228380.ece',
        ]

    def parse(self, response):
        items = CricketItem()

        full_list = response.css('.home-content-p div')
        country = response.css('p:nth-child(1) strong').css('::text').extract_first()
        for player in full_list:
            pname = player.css('.artimgright+ strong , .artimgright+ p strong').css('::text').extract_first()
            img = player.css('.img-responsive::attr(data-proxy-image)').extract_first()

            items['pname'] = pname
            items['img'] = img
            items['country'] = country
            yield items
