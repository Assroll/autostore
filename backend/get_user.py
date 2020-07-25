from config import *
import requests
import urlopen
import json
from firebase import firebase


firebase = firebase.FirebaseApplication(fbase, None)
result = firebase.get('/testy', None)
print(result)
