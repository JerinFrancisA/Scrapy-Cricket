# -*- coding: utf-8 -*-
import scrapy
from ..items import CricketItem


class CricspySpider(scrapy.Spider):
    name = 'cricspy'
    start_urls = [
        'https://www.cricbuzz.com/cricket-team/australia/4/players',
        'https://www.cricbuzz.com/cricket-team/pakistan/3/players',
        'https://www.cricbuzz.com/cricket-team/bangladesh/6/players',
        'https://www.cricbuzz.com/cricket-team/south-africa/11/players',
        'https://www.cricbuzz.com/cricket-team/west-indies/10/players',
        'https://www.cricbuzz.com/cricket-team/sri-lanka/5/players',
        'https://www.cricbuzz.com/cricket-team/new-zealand/13/players',
        'https://www.cricbuzz.com/cricket-team/england/9/players',
        'https://www.cricbuzz.com/cricket-team/afghanistan/96/players',
        ]

    def parse(self, response):
        items = CricketItem()

        full_list = response.css('.cb-col-50')
        country = response.css('.line-ht30::text').extract_first()
        for player in full_list:
            pname = player.css('.text-hvr-underline').css('::text').extract_first()
            img = player.css('.cb-col-27 img').css('::attr(src)').extract_first()

            items['pname'] = pname
            items['img'] = 'https://www.cricbuzz.com' + img
            items['country'] = country
            yield items
