# ur.dsheet: CSV files for managing domain names on Namebase.

### Warning: This repo is for informational and teaching purposes only, and these scripts are for testing purposes only. It's reccomended that you use a test account with top-level domains (TLDs) you don't care for losing. By using these scripts, you agree that I am not responsible for any losses that may be had from such use. 

### Dependencies
- python / python3
- Linux / Ubuntu
- dotenv

Minor changes were made to https://github.com/pretended/namebase-marketplace to best suit the purpose. 

### setup authorizations on your account: input your information into a .env file at the root directory:
"""
namebaseUserEmail = "<your@email>"
namebaseUserPassword = "<yourPassword>"
namebaseMainCookie = "<your"NamebsebaseMain"Cookie>"
"""
for more info on the cookie, see 'Github OAuth bypass and 2FA Auth Bypass' below.

# Using the scripts:
### You can find these scripts in dsheets/scripts and the accompanying csv files in dsheets/csv. For best results, run them in the following order:

- To put domains into a 'domains.csv' file; run in terminal:
"""
python3 domains_to_csv.py
"""

- Setup initial listings of 1000000HNS each for domains in 'domains.csv':
"""
python3 first_listing.py
"""

- Put TLDs currently for sale into 'selling.csv':
"""
python3 forsale_to_csv.py
"""

- To list for specific prices, edit the price for a domain in selling.csv, and run:
"""
python3 update_prices.py
"""

- To batch add dLinks, paste names list under "label" column and run:
"""
python3 add_dlinks.py
"""

- Once you add dLinks, you will need to publish the page for it to be public. To publish a page, run:
"""
python3 publish_dlinks.py
"""

- In development: Put current dLinks into 'dlinks.csv' (currently an unseperated list- fix coming soon), run:
"""
python3 dlinks_to_csv.py
"""

-----------------------------------------
Namebase Marketplace Api for Python
==

<p>
<a href="https://namebase-marketplace.readthedocs.io/en/latest/">
<img src="https://readthedocs.org/projects/namebase-exchange-python/badge/?version=latest" alt="Open Issues"/>
</a>
<a href="/issues">
<img src="https://img.shields.io/github/issues/pretended/namebase-marketplace" alt="Open Issues"/>
</a>
<a href="https://pypi.org/project/namebase-marketplace/">
<img src="https://img.shields.io/pypi/v/namebase-marketplace.svg" alt="PyPI"/>
</a>
<a href="/LICENCE">
<img src="https://img.shields.io/github/license/pretended/namebase-marketplace" alt="MIT Licence"/>
</a>
<img src="https://static.pepy.tech/badge/namebase-marketplace/week"/>

  
Python 3.6+ client for interacting with Namebase Marketplace API.

## Usage
Instantiating the Marketplace object can be done either by using email and password or None.
Only post requests can be made authenticated.

Websocket API is not provided.
## Installation

### Requirements

- Python 3.6 or greater

### Install

> pip install namebase-marketplace

### Usage

##### Core REST API for Namebase MARKETPLACE
```python
from namebase_marketplace.marketplace import *
marketplace = Marketplace(email="YOUR EMAIL", pwd="YOUR PASSWORD")
marketplace.get_user_info()
marketplace.open_bid(domain='domain', bid_amount=0.4, blind_amount=100)
```

##### EXAMPLE WITHOUT AUTHENTICATION:
```python
from namebase_marketplace.marketplace import *
marketplace = Marketplace()
marketplace.get_marketplace_domains(offset=100) # Get 101-200 latest marketplace domains with default options
```

  
On some endpoints you can pass options, please refer them to the following documentation: https://github.com/namebasehq/api-documentation/blob/master/marketplace-api.md

### Github OAuth bypass and 2FA Auth Bypass
You can bypass these restrictions to use this library by replacing the following code on your namebase_marketplace package and marketplace class:
  
  ```python
   self.cookies = { "namebase-main": "s:lF21222EXX2323c-EXAMPLE.THIS_IS_AN_EXAMPLE++121HRYL/23+42c/12hOEEXAMPLE223" } 
```
  
  This is the cookie Namebase uses to auth you within the app. You can find this cookie when reloading any page and going to Network on Inspection Mode. Head to a request and find this cookie under "Cookies" tab on any explorer along with other kind of cookies.

  
### Donations

I have made this library open-sourced and free to use. However, if you consider this library has helped you, or you just want to sponsor me, donations are welcomed to one of my HANDSHAKE addresses. 

> hs1qynh72cuj7lawdcmvjtls4kk0p4auzmj5qq6v3r
