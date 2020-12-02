
import requests
import json
import unittest
import os

url = 'https://itunes.apple.com/search'
page = requests.get(url, params = '')
data = page.json() 
print(data)


try:
    js = json.loads(data)

except:
    print(data)
   

## curr.execute(??)
## curr.commit()


##  

import plotly.express as px
import panda as pd 
