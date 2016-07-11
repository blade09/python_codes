# ----------------------------------------------------------------------------------------------
# IEXT - Image EXtractor Tool
#
# this tool is a image extractor tool which can go ahead and extract all the images which is embedded under the supplied link.
#
# author :  Bunty , version 1.0
# ----------------------------------------------------------------------------------------------


print("""# -----------------------------------------------------------------------------------------------------------------------
# IEXT - Image EXtractor Tool
#
# this tool is a image extractor tool which can go ahead and extract all the images which is embedded under the supplied link.
#
# Author :  Bunty Chakraborty, version 1.0
# ---------------------------------------------------------------------------------------------------------------------------""")
import requests
from bs4 import BeautifulSoup
from urllib.parse import *
from random import randrange
from urllib.request import urlretrieve
import os
import tld
from tqdm import tqdm
from time import sleep


url_from_user=input("Enter the desired url:")
check_link=urlparse(url_from_user)
if "http" not in check_link:
    full_link="http://"+url_from_user
    response=requests.get(full_link)
    soup=BeautifulSoup(response.text,"html5lib")

    image_all=soup.find_all('img')

    for image in image_all:
        
       path=image.get('src')
       url=urljoin(full_link,path)
       local_name=str(randrange(0,1000)) + ".jpg"
       urlretrieve(url,local_name)
       for i in tqdm(range(9)):
           sleep(0.1)
    print("Suceessfully Extracted all the images..... :) ")
        

else:
    response=requests.get(url_from_user)
    soup=BeautifulSoup(response.text,"html5lib")
    image_all=soup.find_all('img')
    for image in image_all:
        path=image.get('src')
        url=urljoin(url_from_user,path)
        local_name=str(randrange(0,1000)) + ".jpg"
        urlretrieve(url,local_name)
        for i in tqdm(range(9)):
            sleep(0.1)
    print("Suceessfully Extracted all the images..... :) ")
       
        
        
     




   
   
    
    

    


