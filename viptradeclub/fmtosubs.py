import telebot
import time
import csv
import traceback
from datetime import datetime,timedelta
import matplotlib.pyplot as plt
import numpy as np


def createstatsgraph():

    with open('stats.csv','r') as fls:
        y=[]
        x1=[]
        x2=[]
        reader=csv.reader(fls)
        for inf in reader:
            y.append(int(inf[3]))
            x1.append(int(inf[0]))
            x2.append(int(inf[1]))
        y.sort()
    
        plt.plot(y,x1,color='blue')
        plt.fill_between(y,x1, np.zeros_like(x1), color='cyan')

        plt.plot(y,x2,color='red')
        plt.fill_between(y,x2, np.zeros_like(x2), color='pink')

        plt.xlabel('Месяц')
        plt.ylabel('Количество пользователей\n(заблокировавшие бота(красным),не заблокировавшие(синим))')
        
        plt.savefig('stats.png')

token='2016291523:AAGjdHizngiA3ZcXk6z1ayw9KNU-CPp268c'#write your bot token here
asyncbot=telebot.TeleBot(token)
start_time = datetime.now()
previousid=None

def listofusers():
    users=[]
    with open('userdb.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            users.append(row[0])
    return users

def blckedusers():
    blusers=[]
    with open('blockedusers.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            blusers.append(row[0])
    return blusers

while 1:
    current_datetime = datetime.now()
    with open('messagetosubs.txt','r') as fl:
        for row in fl:
            if row != None and row!=previousid:
                previousid=row
                with open('userdb.csv') as fil:
                    reader = csv.reader(fil)
                    for chatid in reader:
                        try:
                            asyncbot.forward_message(int(chatid[0]),1974035984,int(row) )
                        except:
                            time.sleep(1)
                            try:
                                asyncbot.forward_message(int(chatid[0]),1974035984,int(row))
                            except:
                                with open('blockedusers.csv','a') as bu:
                                    writer = csv.writer(bu)
                                    writer.writerow(chatid)
    timeres = datetime.now()-start_time
    if timeres.seconds > 86400:
        start_time = datetime.now()
        with open('stats.csv','a') as f:
            writer = csv.writer(f)
            writer.writerow([len(set(listofusers())), len(set(blckedusers())), start_time.month, start_time.day])
        stats = []
        with open('stats.csv','r') as sf:
            reader = csv.reader(sf)
            for row in reader:
                stats.append(row)
        createstatsgraph()


