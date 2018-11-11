import sys


sys.path.insert(1, '.')
from crawl.crawler import Crawler


class GSMAreanaReviewCrawler:
    def __init__(self, url):
        self.url = url

    def crawl(self):
        soup = Crawler.get_soup(self.url)
        self.url = 'http://www.gsmarena.com/' + soup.find('a', text='Read all opinions')['href']
        soup = Crawler.get_soup(self.url)
        review_page_count = int(soup.find('div', {'id': 'user-pages'}).findAll('a')[-2].getText())

        url = self.url
        for i in range(2, review_page_count):
            reviews = soup.findAll('p', {'class': 'uopin'})
            for r in reviews:
                for tag in r.findAll('a'):
                    tag.replaceWith('')

                for tag in r.findAll('span'):
                    tag.replaceWith('')

                print(r.getText().strip())

            url = self.url.replace('.php', 'p%d.php' % i)
            soup = Crawler.get_soup(url)


# Example
# Crawling reviews about sumsung galaxy note 5
GSMAreanaReviewCrawler('https://www.gsmarena.com/samsung_galaxy_note5-7431.php').crawl()