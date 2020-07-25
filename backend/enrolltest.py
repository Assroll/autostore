from config import *
import requests
import urlopen
from firebase import firebase


# put your keys in the config.py


# Switch url for what you are doing (Enroll, verify etc)
url = "http://api.kairos.com/enroll"
firebase = firebase.FirebaseApplication(
    'https://autoshop-205c2.firebaseio.com/', None)

payload = """
  {
    "image":"https://www.eiendomsmegler1.no/fileshare/fileupload/14933/Christer%20Hagen2.jpg?width=659&height=659&upscale=True&crop=True&x=1368&y=0&scale=0,16436991532458908",
    "subject_id": "Christer",
    "gallery_name": "MyGallery"
  }
"""


request = requests.post(url, data=payload, headers=headers)

requestq = print(request.content)
print(request.content)

result = firebase.post('/users2', requestq, params={'print': 'pretty'})
print(result)
