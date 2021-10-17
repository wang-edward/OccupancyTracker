import requests
from firebase import firebase
from datetime import datetime
import time
# import firebase_admin
# from firebase_admin import credentials
firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)

text = 'edad'


number_of_people = 213

#creates new folder for number of people at that time
def update_db(num_people):
    cur_time = str(int(time.time()))
    print (cur_time)
    firebase.post(cur_time, num_people)





update_db(number_of_people)