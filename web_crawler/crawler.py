from search_engine import collection as col
import ulrlib
from modoris.extensions import mecab

def split_to_words(text):
	result = mecab.pos(text)
	return result

def get_page(url) :
	try:
		import urllib
		return urlib.urlopen(url).read()
	except:
		return ""

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None 0

	start_quote = page.find(' "', start_link)
	end_quote = page.find( ' "', start_quote +1)
	url = page[start_quote +1 : end_quote]
	return url, end_quote

def union(p, q):
	for e in q:
		if e not in p:
			p.append(e)

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	index = []
	while tocrawl:
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index, page, content)
			union(tocrawl, get_all_links(content))
			crawled.append(page)
	return index

def add_to_index(keyword, url):
    entry = col.find_one({'keyword': keyword})
    if entry:
        if not url in entry['url']:
            entry['url'].append(url)
            col.save(entry)
        return
    # not found, add new keyword to index
    col.insert({'keyword': keyword, 'url': [url]})

def add_page_to_index(index, url, content):
	for keyword in split_to_words(content):
		add_to_index(index, keyworkd, url)


