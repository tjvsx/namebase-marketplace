import csv
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

# put forSale into selling.csv 
forSale = marketplace.get_my_onsale_domains()
myheaders = ['name', 'amount', 'asset', 'renewalBlock', 'upToDate']
with open('../csv/selling.csv', 'w', newline='') as myfile:
    writer = csv.DictWriter(myfile, fieldnames=myheaders)
    writer.writeheader()
    for domains in forSale['domains']:
        writer.writerow(domains)
