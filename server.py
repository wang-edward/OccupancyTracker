import requests
from firebase import firebase
from datetime import datetime 
from datetime import date
import time
import matplotlib
import json
# import firebase_admin
# from firebase_admin import credentials
firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)

text = 'edad'


number_of_people = 213
cur_time = str(int(time.time()))
cur_date = date.today().strftime("/%Y/%m/%d/")

def update_time():
    cur_time = str(int(time.time()))
    cur_date = date.today().strftime("/%Y/%m/%d/")

#creates new folder for number of people at that time
def update_db(num_people):
    update_time()

    index = cur_date + cur_time

    print(index)

    firebase.post(index, num_people)

def graph():
    update_time()
    results = firebase.get(cur_date, None)
    print(results)
    for value in results:
        print((results[value])[0])



# update_db(number_of_people)
graph()
    
# print(cur_date)