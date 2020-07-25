from config import *
import requests
import urlopen
from firebase import firebase
import json

# Switch url for what you are doing (Enroll, verify etc)
url = "http://api.kairos.com/enroll"
firebase = firebase.FirebaseApplication(fbase, None)

payload = """
  {
    "image":"https://media.kairos.com/liz.jpg",
    "subject_id": "Christer",
    "gallery_name": "MyGallery"
  }
"""

request = requests.post(url, data=payload, headers=headers)
request.json()

result = firebase.post('/testy', request.json())
print(result)
