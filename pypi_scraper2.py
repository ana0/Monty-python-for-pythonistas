import urllib2
from bs4 import BeautifulSoup
from scraped import scraped

def assemble_link_list(parsed_webpage):
    all_links = []
    for item in parsed_webpage:
        for link in item.find_all('a'):
            all_links.append(link.string)
    return all_links

def get_index_nums(link_list):
    ending_nums = [filter_end_digits(i) for i in link_list]
    return [i for i in ending_nums if len(i) > 0 and len(i) < 4]

def filter_end_digits(url, index_num=""):
    if url[-1:].isdigit():
        index_num = url[-1:] + index_num
        return filter_end_digits(url[0:-1], index_num=index_num)
    return index_num

# pypiurl = "https://pypi.python.org/pypi?:action=browse&show=all&c=228"
# request = urllib2.urlopen(pypiurl)
# soup = BeautifulSoup(request, "html.parser")

# package_table = soup.find_all("table", {"class":"list"})
# all_links_in_table = assemble_link_list(package_table)

def catch_em_all(all_package_pages):
    for index_num in all_package_pages:
        url = "https://pypi.python.org/pypi?:action=browse&show=all&c=" + index_num
        request = urllib2.urlopen(url)
        soup = BeautifulSoup(request, "html.parser")
        package_table = soup.find_all("table", {"class":"list"})
        all_links_in_table = assemble_link_list(package_table)
        f = open('all_packages.txt', 'a')
        for link in all_links_in_table:
            f.write(link)

# f = open('all_packages.txt', 'a')
# for link in all_links_in_table:
#     f.write(link +"\n")

catch_em_all(scraped)