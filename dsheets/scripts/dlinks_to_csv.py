import csv
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

# puts dlinks into dlinks.csv 
domainLinks = marketplace.get_dlinks()
myheaders = ['href', 'label', 'isEnabled']
with open('../csv/dlinks.csv', 'w', newline='') as myfile:
    writer = csv.DictWriter(myfile, fieldnames=myheaders)
    writer.writeheader()
    for dLinks in domainLinks['dLinks']:
        for links in dLinks['links']:
            writer.writerow(links)

