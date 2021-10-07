import csv
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

#get list of names using csv.DictReader
inpath = Path("../csv/selling.csv")

with inpath.open("r", newline="", encoding="utf-8-sig") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        domains = f"{row['name']}"
        amount = f"{row['amount']}"
        marketplace.update_domain(domain=domains, amount=amount, description='for more great prices, go to xdomains.hns.to')

