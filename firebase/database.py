
import requests
from firebase import firebase


firebase = firebase.FirebaseApplication('https://autoshop-205c2.firebaseio.com/', None)
new_user = 'Ozgur Vatansever'

result = firebase.post('/gamers', new_user, params={'print': 'pretty'})
print(result)


#result = firebase.post('/users', new_user, {'print': 'silent'}, {'X_FANCY_HEADER': 'VERY FANCY'})
#print(result) == None
#True

