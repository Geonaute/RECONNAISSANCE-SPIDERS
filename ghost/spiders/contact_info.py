import scrapy 
import re
from ghost.items import GhostItem

class infoSpider(scrapy.Spider):
	name = 'contact_information'
	allowed_domains = [
		'http://www.azparanormalcowboys.com',
		'http://www.moonconnection.com',
		'http://www.freecounterstat.com',
		'http://www.topparanormalsites.com/',
	]
	with open('url_list.csv') as f:
		start_urls = [url.strip() for url in f.readlines()]
		
	def parse(self, response):
		text = str(response.xpath('*').extract())
		email_regex = re.findall(r'[\w\.-]+@[\w\.-]+', text)
		phone_regex = re.findall(r'\(?\b[0-9]{3}\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}\b', text)
		item = GhostItem(email = email_regex, phone = phone_regex)
		yield item
