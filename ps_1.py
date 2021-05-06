import requests
import urllib

# URL for old "Grandstand 4600 consoles - S O L D "
url = "https://www.ebay.co.uk/sch/i.html"

# Headers from Chrome Version 90.0.4430.93 (Official Build) (64-bit)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "referer": "https://www.ebay.co.uk",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    "sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site"
}

params = {'_nkw': 'grandstand+4600', 
          '_in_kw':'1', 
          '_ex_kw':'',
          '_sacat':'0',
          'LH_Sold':'1',
          '_dlo' :'',
          '_udhi':'',
          '_samilow':'',
          '_samihi':'',
          '_sadis':'15',
          '_sargn':'-1%26saslc%3D1',
          '_salic':'3',
          '_sop':'12',
          '_dmd':'1',
          '_ipg':'200',
          'LH_Complete':'1',
          '_fosrp':'1'
          }

res = requests.get(url, headers=headers,params=params)
print(res.url)