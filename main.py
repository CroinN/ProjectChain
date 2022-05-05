from email import message
from inspect import _empty
from logging import debug
from pickle import FALSE
from random import random
import string
import random
import this
from xmlrpc.client import boolean


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

stage=0

bot = Bot(token='5316993267:AAEy6Pqkt7c8fIKpXedwtIe8BSwdnntRoag')


dp=Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message : types.message):
    await message.reply("Password please :)")

@dp.message_handler(commands=['wish'])
async def wish(message : types.message):
    global stage
    if(stage==1):
        File=open("current_info.txt","r")
        wish=File.readlines()[0]
        if(wish==""):
            print("no wish")
        else:
            await message.reply(wish)
        stage=2

@dp.message_handler()
async def try_password(message : types.message):
    global stage 
    if(stage==0):
        passwordCheck=PasswordCheck(message)
        if(passwordCheck==0):   
            await message.reply("true password write /wish")
            stage=1
        else:
            if(passwordCheck==1):
                await message.reply("wrong password try again")
            if(passwordCheck==2):
                await message.reply("already used id")
    if(stage==2):
        await message.reply(NewWish(message))
        stage=0
        



def NewWish(msg):
    msgtxt=msg.text

    File=open("current_info.txt","r")
    arr=File.readlines()
    arr[0]=msgtxt+"\n"
    File=open("current_info.txt","w")
    newPassword=GetNewPassword()
    arr[1]=newPassword+"\n"

    File.writelines(arr)
    File=open("users.txt","r")
    arr=File.readlines()
    arr.__iadd__(str(msg.chat.id)+"\n")
    File=open("users.txt","w")
    File.writelines(arr)

    return newPassword

def PasswordCheck(msg):
    if(CheckUsers(msg.chat.id)):
        return 2
    File=open("current_info.txt","r")
    arr=File.readlines()
    msgtxt=msg.text+"\n"
    if(arr[1]==msgtxt):
        File=open("current_info.txt","w")
        arr[2]=str(msg.chat.id)
        File.writelines(arr)
        return 0
    else:
        return 1
    # 0-chishta
    # 1-sxal parol
    # 2-arden ogtgorcvac id       

def GetNewPassword():
    characters=list(string.ascii_letters+string.digits)
    random.shuffle(characters)
    password=[]
    for i in range(8):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password) 

def CheckUsers(current_id):
    id=str(current_id)+"\n"
    File=open("users.txt","r")
    arr=File.readlines()
    for i in arr:
        if(id==i):
            return True
    return False
    


executor.start_polling(dp, skip_updates=False)