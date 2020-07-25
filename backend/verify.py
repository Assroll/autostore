from config import *
import requests
import urlopen
import json

# put your keys in the header config.py

# Switch url for what you are doing (Enroll, verify etc)
url = "http://api.kairos.com/verify"


payload = """
  {
    "image": "https://g.acdn.no/obscura/API/dynamic/r1/ece5/tr_1080_717_l_f/0000/avno/2016/9/2/18/02NYHChrister%2BHagen%2B01_02-0_1.jpg?chk=870DFC",
    "gallery_name": "MyGallery",
    "subject_id": "Christer"
  }
"""

request = requests.post(url, data=payload, headers=headers)

print(request.json())
