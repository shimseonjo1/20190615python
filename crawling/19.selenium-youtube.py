from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
import sys

driver = wd.Chrome(executable_path='./crawling/data/chromedriver')
filters = {
    'hour': 'EgQIARAB', # 지난 한시간
    'today': 'EgQIAhAB', # 오늘
    'week': 'EgQIAxAB', # 이번주
    'month': 'EgQIBBAB', #이번달
    'year': 'EgQIBRAB' #올해
}
word = 'BTS'
url = 'https://www.youtube.com/results?search_query={word}&sp={date}'.format(word=word, date=filters['today'])
driver.get(url)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('h3 > a#video-title')
print(titles)
'''
def getVideoElement():
    return driver.find_elements_by_tag_name('ytd-video-renderer')

print(getVideoElement())

def getVideoCount():
    return len(getVideoElement())

print(getVideoCount())
'''
driver.close()
driver.quit()
sys.exit()