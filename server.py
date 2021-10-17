from firebase import firebase
from datetime import datetime 
from datetime import date
import matplotlib.pyplot as plt

firebase = firebase.FirebaseApplication('https://occupancytracker-69a70-default-rtdb.firebaseio.com/', None)

cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
cur_date = date.today().strftime("/%Y/%m/%d/")

#creates new folder for number of people at that time
def update_db(num_people):
    cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
    cur_date = date.today().strftime("/%Y/%m/%d/")
    index = cur_date + "/" + cur_time

    firebase.post(index, num_people)

def graph():
    cur_time = str(datetime.now().time().strftime("%H:%M:%S:%f"))
    cur_date = date.today().strftime("/%Y/%m/%d/")

    results = firebase.get(cur_date, None)

    answer_num = [] #output list
    answer_time = []

    for temp in results:
        for key, value in results[temp].items():
            answer_num.append(value)
            answer_time.append(temp)

    fig, ax = plt.subplots()
    ax.plot(answer_time,answer_num)
    plt.show()
    
