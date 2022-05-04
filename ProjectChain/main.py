from inspect import _empty
from logging import debug
from pickle import FALSE
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
    await message.reply("asa parol@")

@dp.message_handler(commands=['wish'])
async def wish(message : types.message):
    global stage
    if(stage==1):
        wishesFile=open("wishes.txt","r")
        msg=wishesFile.read()
        if(msg==""):
            print("empty txt file")
        else:
            await message.reply(msg)
        stage=2

@dp.message_handler()
async def try_password(message : types.message):
    global stage 
    if(stage==0):
        if(message.text =="1111"):   
            await message.reply("chishta")
            stage=1
        else:
            await message.reply("sxala")
    if(stage==2):
        wishesFile=open("wishes.txt","w")
        wishesFile.write(message.text)
        stage=3
        

  

executor.start_polling(dp, skip_updates=False)