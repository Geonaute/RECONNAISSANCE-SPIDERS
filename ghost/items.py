# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GhostItem(scrapy.Item):
	email = scrapy.Field()
	phone = scrapy.Field()
class GhostLinks(scrapy.Item):
	SiteLinks = scrapy.Field()
