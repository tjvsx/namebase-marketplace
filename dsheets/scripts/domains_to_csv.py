import csv
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

# put myDomains into domains.csv 
myheaders = ['name', 'renewalBlock', 'upToDate', 'numberViews', 'usesOurNameservers']
myDomains = marketplace.get_my_domains()
with open('../csv/domains.csv', 'w', newline='') as myfile:
	writer = csv.DictWriter(myfile, fieldnames=myheaders)
	writer.writeheader()
	writer.writerows(myDomains)

