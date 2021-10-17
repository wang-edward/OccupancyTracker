import requests
from firebase import firebase
from datetime import datetime
import time

firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)

#creates new folder for number of people at that time
def update_db(num_people):
    cur_time = str(int(time.time()))
    firebase.post(cur_time, num_people)
