import scrapy
class GhostItem(scrapy.Item):
	email = scrapy.Field()
	phone = scrapy.Field()
class GhostLinks(scrapy.Item):
	SiteLinks = scrapy.Field()
