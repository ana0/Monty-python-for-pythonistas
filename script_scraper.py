


import urllib2
from bs4 import BeautifulSoup

def catch_em_all():
    for i in range(1, 46):
        if i < 10:
            url = "http://www.ibras.dk/montypython/episode0" + str(i) + ".htm"
        else:
            url = "http://www.ibras.dk/montypython/episode" + str(i) + ".htm"
        print "scraping " + url
        #make request
        request = urllib2.urlopen(url)
        soup = BeautifulSoup(request, "html.parser")
        script_table = soup.find_all("td")
        #add them all to a huge file
        f = open('all_scripts.txt', 'a')
        for column in script_table:
            line = column.get_text()
            f.write(line.encode('utf-8'))
        f.close()

#make request
request = urllib2.urlopen("http://www.intriguing.com/mp/_scripts/meanlife.php")
soup = BeautifulSoup(request, "html.parser")
script = soup.get_text("td")

#add them all to a huge file
f = open('all_scripts.txt', 'a')
f.write(script.encode('utf-8'))
f.close()

