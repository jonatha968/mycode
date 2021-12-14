#1/usr/bin/env python3

#import necessary componants
import shutil
import os

#Start in the right directory
os.chdir("/home/student/mycode/mycode/")

#Copy files from source to destination
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

#Copy a full directory from srouce to destination
shutil.copytree("5g_research/", "5g_research_backup/")



