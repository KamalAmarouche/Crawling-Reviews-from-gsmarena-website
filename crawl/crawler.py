
from bs4 import BeautifulSoup

import urllib.request


class Crawler:


	def get_soup(url):
		soup = None
		try:
			request = urllib.request.urlopen(url)
			page = request.read()
			soup = BeautifulSoup(page, 'html.parser')
		except ValueError:
			print('Failed to read webpage : %s' % ValueError)

		return soup