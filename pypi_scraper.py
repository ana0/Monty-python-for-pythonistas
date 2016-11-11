import urllib2
from bs4 import BeautifulSoup

def assemble_link_list(parsed_webpage):
    all_links = []
    for link in parsed_webpage.find_all('a'):
        all_links.append(link.get('href'))
    return all_links

def get_index_nums(link_list):
    ending_nums = [filter_end_digits(i) for i in link_list]
    return [i for i in ending_nums if len(i) > 0 and len(i) < 4]

def filter_end_digits(url, index_num=""):
    if url[-1:].isdigit():
        index_num = url[-1:] + index_num
        return filter_end_digits(url[0:-1], index_num=index_num)
    return index_num

pypiurl = "https://pypi.python.org/pypi?%3Aaction=browse"
request = urllib2.urlopen(pypiurl)
soup = BeautifulSoup(request, "html.parser")

all_links_on_page = assemble_link_list(soup)
all_index_nums = get_index_nums(all_links_on_page)

f = open('scraped.txt', 'w')
f.write(str(all_index_nums))

