import os
os.system('scrapy crawl contact_information -o contact.csv')
os.system('python contact_filter.py')
