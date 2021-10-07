import csv
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('../../')

from namebase_marketplace.marketplace import *
marketplace = Marketplace(email=os.environ.get("namebaseUserEmail"), pwd=os.environ.get("namebaseUserPassword"))

#################################
pageAddress = "xpedio"
#################################

params = {"fullDomainName": pageAddress}

req = marketplace.publish_dlinks(params=params)

print(req)

