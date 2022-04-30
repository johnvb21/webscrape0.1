import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

def sort_by_votes(hnlist):
	return sorted(hnlist, key= lambda k:k['votes'], reverse=True)


def sort_the_news(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')

		if len(vote):
			points = int(vote[0].getText().replace('points',''))
			if points > 99:
				hn.append({'title': title, 'link': href, 'votes': points})
	return hn

def sort_the_news2(links2, subtext2):
	hn2 = []
	for idx, item in enumerate(links2):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext2[idx].select('.score')

		if len(vote):
			points = int(vote[0].getText().replace('points',''))
			if points > 99:
				hn2.append({'title': title, 'link': href, 'votes': points})
	return hn2

list1 = sort_the_news(links, subtext)
list2 = sort_the_news2(links2, subtext2)
list3 = list1 + list2
list3 = sort_by_votes(list3)
pprint.pprint(list3)