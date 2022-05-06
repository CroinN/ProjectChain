from email import message
from inspect import _empty
from logging import debug
from pickle import FALSE
from random import random
import this
from xmlrpc.client import boolean


from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

import functions

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
        arr=File.readlines()
        if(arr[2]==str(message.chat.id)):
            wish=arr[0]
            if(wish==""):
                print("no wish")
            else:
                await message.reply(wish)
            stage=2
        else:
            await message.reply("Bot is being used by other user")
    else:
        await message.reply("Password please :)")        

@dp.message_handler()
async def try_password(message : types.message):
    global stage 
    if(stage==0):
        passwordCheck=functions.PasswordCheck(message)
        if(passwordCheck==0):   
            await message.reply("True password /wish")
            stage=1
        else:
            if(passwordCheck==1):
                await message.reply("Wrong password try again")
            if(passwordCheck==2):
                await message.reply("Already used id")
    if(stage==2):
        await message.reply("New Password")
        await message.reply(functions.NewWish(message))
        stage=0
        

async def Message(msg):
    await bot.send_message(msg)


executor.start_polling(dp, skip_updates=False)