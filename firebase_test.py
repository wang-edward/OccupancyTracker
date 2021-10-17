import requests
from firebase import firebase

firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)

text = 'edad'

test = firebase.post('/', text)