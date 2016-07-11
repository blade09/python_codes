# ----------------------------------------------------------------------------------------------
# FDE - File Downloader Engine
#
# this tool is a file downloader tool which can go ahead and download the file which is embedded under the supplied link.

# Usage:Accept Command line argument:

# py file_downloader.py <full_path> (for windows)

# python file_downloader.py <full_path>(for linux)

# ./file_donwnloader <full_path>(for linux)

# Author: Bunty Chakraborty , version 1.0
# ----------------------------------------------------------------------------------------------




print("""# ----------------------------------------------------------------------------------------------
# FDE - File Downloader Engine
#
# this tool is a image extractor tool which can go ahead and extract all the images which is embedded under the supplied link.

# Usage:Accept Command line argument:

# py file_downloader.py <full_path> (for windows)

# python file_downloader.py <full_path>(for linux)

# ./file_donwnloader <full_path>(for linux)

# Author: Bunty Chakraborty , version 1.0
# ----------------------------------------------------------------------------------------------

""")

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

