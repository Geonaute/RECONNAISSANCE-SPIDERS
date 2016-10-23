with open('url_list.csv') as f:
		urls = [url.strip() for url in f.readlines()]
urls = list(set(urls))
with open('url_list.csv', 'w') as f:
	for item in urls:
		f.write("%s\n" % item)
