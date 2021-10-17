import requests
from firebase import firebase
from datetime import datetime 
from datetime import date
import time
import matplotlib.pyplot as plt
import numpy as np
import json
# import firebase_admin
# from firebase_admin import credentials
firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)


number_of_people = 213
cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
cur_date = date.today().strftime("/%Y/%m/%d/")

# def update_time():
#     # cur_time = str(int(time.time()))
#     cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
#     cur_date = date.today().strftime("/%Y/%m/%d/")

#creates new folder for number of people at that time
def update_db(num_people):
    # update_time()
    cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
    cur_date = date.today().strftime("/%Y/%m/%d/")
    index = cur_date + "/" + cur_time

    firebase.post(index, num_people)



def graph():
    cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
    cur_date = date.today().strftime("/%Y/%m/%d/")
    update_time()
    results = firebase.get(cur_date, None)

    answer_num = [] #output list
    answer_time = []

    for temp in results:
        for key, value in results[temp].items():
            answer_num.append(value)
            answer_time.append(temp)

    for x in answer_time:
        print(x)
    for i in answer_num:
        print(i)

    fig, ax = plt.subplots()
    ax.plot(answer_time,answer_num)
    plt.show()
    

# testing!!! -------------------------------------------------

# update_db(number_of_people)
graph()
