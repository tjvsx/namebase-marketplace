import csv
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

##################################
pageTitle = "xpediator"
pageAddress = "xpedio"
##################################

dsheet = []

inpath = Path("../csv/dlinks.csv")
with inpath.open("r", newline="", encoding="utf-8-sig") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
    	label = f"{row['label']}"
    	href = "https://www.namebase.io/domains/" + label
    	rows = {'href': href, 'label': label, 'isEnabled': True}
    	dsheet.append(rows)

params = {"name": {"content": pageTitle, "isEnabled": True}, "backend": "sia", "theme": {"primaryColor": "#FFFFFF", "secondaryColor": "#000000"}, "links": dsheet, "fullDomainName": pageAddress}

req = marketplace.put_dlinks(params=params)

print(req)


