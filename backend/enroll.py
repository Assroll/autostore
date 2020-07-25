
import requests
import urlopen

# put your keys in the header
headers = {
    "Content-Type": "application/json",
    "app_id": "15fd50b7",
    "app_key": "bdaf7ffa5e41f3fa8159286192368710"
}
# Switch url for what you are doing (Enroll, verify etc)
url = "http://api.kairos.com/enroll"

payload = """
  {
    "image":"https://www.eiendomsmegler1.no/fileshare/fileupload/14933/Christer%20Hagen2.jpg?width=659&height=659&upscale=True&crop=True&x=1368&y=0&scale=0,16436991532458908",
    "subject_id": "Christer",
    "gallery_name": "MyGallery"
  }
"""


request = requests.post(url, data=payload, headers=headers)

print(request.content)
