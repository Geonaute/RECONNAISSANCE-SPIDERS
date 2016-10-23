import scrapy
from ghost.items import GhostLinks

class urlSpider(scrapy.Spider):
	name = 'urls'
	allowed_domains = [
		'http://www.azparanormalcowboys.com',
		'http://www.moonconnection.com',
		'http://www.freecounterstat.com',
		'http://www.topparanormalsites.com/',
	]

	with open('url_list.csv') as f:
		start_urls = [url.strip() for url in f.readlines()]

	
	def parse(self, response):
		links = response.xpath('*//@href').extract()
		check_dict = {
					'azpar': 'http://www.azparanormalcowboys.com/',
					'moon': 'http://www.moonconnection.com/',
					'free': 'http://www.freecounterstat.com/',
					'topp': 'http://www.topparanormalsites.com/',
		}
		
		def item_format(url, directory):
			item = GhostLinks(SiteLinks = (str(url) + str(directory)))
			return item
			
		def check(word):
			if word in str(response.url):
				return True
			else: return False
			
		for link in links:
			if 'www' in link:
				yield item_format(link, '')
				
			else:
				for i in check_dict:
					if check(i):
						yield item_format(check_dict[i], link)
		
					
