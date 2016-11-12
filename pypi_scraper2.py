
import urllib2
from bs4 import BeautifulSoup
from scraped import scraped

def assemble_link_list(parsed_webpage):
    all_links = []
    for item in parsed_webpage:
        for link in item.find_all('a'):
            all_links.append(link.string)
    return all_links

def catch_em_all(all_package_pages):
    for index_num in all_package_pages:
        url = "https://pypi.python.org/pypi?:action=browse&show=all&"
            "c=" + index_num
        print "scraping " + url
        #make request
        request = urllib2.urlopen(url)
        soup = BeautifulSoup(request, "html.parser")
        package_table = soup.find_all("table", {"class":"list"})
        #assemble all the links from the table 
        all_links_in_table = assemble_link_list(package_table)
        print "found " + str(len(all_links_in_table)) + " links"
        #add them all to a huge file
        f = open('all_packages.txt', 'a')
        for link in all_links_in_table:
            f.write(link+"\n")
        f.close()

catch_em_all(scraped)