# Make a new user inn Firebase
from config import *
import requests
import urlopen
import json
from firebase import firebase


url = "http://api.kairos.com/enroll"
firebase = firebase.FirebaseApplication(fbase, None)

payload = """
  {
    "image":"https://www.eiendomsmegler1.no/fileshare/fileupload/14933/Christer%20Hagen2.jpg?width=659&height=659&upscale=True&crop=True&x=1368&y=0&scale=0,16436991532458908",
    "subject_id": "Christer",
    "gallery_name": "MyGallery"
  }
"""

request = requests.post(url, data=payload, headers=headers)
request.json()

result = firebase.post('/users2', request.json())
print(result)
