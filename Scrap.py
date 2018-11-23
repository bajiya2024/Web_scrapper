import requests
from bs4 import BeautifulSoup
r = requests.get("http://www.ndtv.com/offbeat/saina-nehwal-tweets-hilarious-video-of-her-mad-sister-prepare-to-rofl-1658104?pfrom=home-specialevent")
soup = BeautifulSoup(r.text)


#(1)First apply method get a html in the system which should we want

print(soup.prettify ())
print(soup.find_all("a"))
for link in soup.find_all("a"):
    #Get the all information about text that use in the website
    "<a href='%s'>%s</a>"%(link.get("href"),link.text)


#2)Second apply method 
#another operation that find out the all details about class footer2014 in div ta
g_data=soup.find_all("div",{"class":"footer2014"})
for item in g_data:
    item.text



#(3)Third apply method      
#when we want to find out the first element in the footer2014 class then we use
for item in g_data:
    print(item.contents[0].text)

#(4)Fourth apply method
for item in g_data:
    print(item.contents[0].find_all("a",{"class","footer2014"}))

    
