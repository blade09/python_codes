'''
Author:Bunty Chakraborty
Usage:Accept Command line argument:
py file_downloader.py <full_path> (for windows)
/*
python file_downloader.py <full_path>(for linux)
./file_donwnloader <full_path>(for linux)

*/

'''

import sys
import random
import urllib.request
import time
def progress(nblock,block_s,file_size):
    i=((nblock*block_s)*100)/float(file_size)
    u="%"
    sys.stdout.write('Downloaded........%f%s\r' % (i,u))
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\b')
        
        
    
x=(sys.argv[1])
listt=["Untitle","Complete","New","Current"]
text="""ahfkjhakfhakflkajflksajlkjslkfjsLAJSFLKAJSLFKCNNLAKNFLMMMSMDKALIIDiiiskjfleooojdniHHdkajldlka;lkd;a
klajdladjladuuudbweixjsnkfkxcbksslfalfhasfkjasfbaskjfbkjasb"""


length=len(x)
ex=length-3
extension=x[ex:length]
local=random.choice(listt)+text[random.randrange(1,4):random.randrange(5,18)]+ str(random.randrange(0,100))+ "."+extension
urllib.request.urlretrieve(x,local,progress)

