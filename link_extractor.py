# ----------------------------------------------------------------------------------------------
# ILD - Important Link Downloader
#
# this  is a link extractor tool which can go ahead and extract all the links which is embedded under the supplied link.

# Usage:Accept Command line argument:

# py link_extractor.py <full_path> (for windows)

# python link_extractor.py <full_path>(for linux)

# ./link_extractor <full_path>(for linux)

# Author: Bunty Chakraborty , version 1.0
# ----------------------------------------------------------------------------------------------



print("""# ----------------------------------------------------------------------------------------------
# ILD - Important Link Downloader
#
# this  is a link extractor tool which can go ahead and extract all the links which is embedded under the supplied link.

# Usage:Accept Command line argument:

# py link_extractor.py <full_path> (for windows)

# python link_extractor.py <full_path>(for linux)

# ./link_extractor <full_path>(for linux)

# Author: Bunty Chakraborty , version 1.0
# ----------------------------------------------------------------------------------------------
""")







#importing modules
import sys
import os
import urllib.request
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup

#Requesting the webpage by http request and response object
x=str(sys.argv[1])
request=Request(x)
response=urlopen(request)


#file object creation to store our links
file=open('links.txt','w+')
#Invoking beautifulsoup

soup=BeautifulSoup(response.read(),'html5lib')

for all_links in soup.find_all('a'):
    text=all_links['href']
    file.write(text)
    print(all_links['href'])

print("All links are currently saved in a text file(name:%s) which located in the following path" %"links")

print("#################################################")
print(os.getcwd())

print("#################################################")
file.close()
    
    



