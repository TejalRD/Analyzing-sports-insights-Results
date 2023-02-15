# from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask import render_template
from flask import request
# import pandas as pd
from datetime import datetime
import json
import pandas as pd
import matplotlib.pyplot as plt
from reddit_per_day import get_data
from player_popularity import get_count,get_names,players

app = Flask(__name__ ,template_folder='templates')

@app.route('/home')  
def home():  
    return render_template('home.html');  

@app.route("/reddit_per_day")
def reddit_per_day():
    values = get_data()
    hours = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    legend = 'idk something nice'
    return render_template('chart.html', values=values, labels=hours, legend=legend)


@app.route('/player_popularity', methods =["GET", "POST"])
def player_popularity():
    
    values = get_count()
    labels = get_names()
    if request.method == "POST":
        
        first_name = request.form.get("fname")
        count = players(first_name)
        print("prev: ",labels, count)
        labels.append(first_name)
        print("new: ",labels)
        print("new: ",values)
        values.append(count)
   
    print("new2: ",labels)
    print("new2: ",values)
    return render_template('chart.html', rvalues=values[0],tvalues=values[1],yvalues=values[2], labels=labels)

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask
# from flask import render_template
# from datetime import time


# app = Flask(__name__ ,template_folder='templates')
# word1 = "Suryakumar"
# word2 = "Rizwan"
# word3 = "Conway"
# word4 = "Babar"
# rcount = [0,0,0,0]
# with open("reddit_cricket.csv",encoding='UTF-8') as f2:
#     for line in f2:
#         words = line.split()
#         for i in words:
#             if(i==word1):
#                 rcount[0]+=1
#             if (i==word2):
#                 rcount[1]+=1
#             if (i==word3):
#                 rcount[2]+=1
#             if (i==word4):
#                 rcount[3]+=1
# reddit=[rcount[0],rcount[1],rcount[2],rcount[3]]
# print(reddit)

# @app.route("/simple_chart")
# def chart():
#     legend = 'Monthly Data'
#     # labels = ["January", "February", "March", "April", "May", "July", "August","September"]
#     labels = ['Suryakumar','Rizwan','Conway','Babar']
#     # values = [10, 9, 8, 7, 6, 4, 7, 8]
#     values = reddit
#     return render_template('line_chart.html', values=values, labels=labels, legend=legend)


# # @app.route("/line_chart")
# # def line_chart():
# #     legend = 'Temperatures'
# #     temperatures = [73.7, 73.4, 73.8, 72.8, 68.7, 65.2,
# #                     61.8, 58.7, 58.2, 58.3, 60.5, 65.7,
# #                     70.2, 71.4, 71.2, 70.9, 71.3, 71.1]
# #     times = ['12:00PM', '12:10PM', '12:20PM', '12:30PM', '12:40PM', '12:50PM',
# #              '1:00PM', '1:10PM', '1:20PM', '1:30PM', '1:40PM', '1:50PM',
# #              '2:00PM', '2:10PM', '2:20PM', '2:30PM', '2:40PM', '2:50PM']
# #     return render_template('line_chart.html', values=temperatures, labels=times, legend=legend)




# if __name__ == "__main__":
#     app.run(debug=True)
