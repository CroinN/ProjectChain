from email import message
import fileinput
from inspect import _empty
from logging import debug
from msilib.schema import File
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

@dp.message_handler(commands=['msg'])
async def msg(message : types.message):
    global stage
    if(stage==1):
        File=open("current_info.txt","r")
        arr=File.readlines()
        if(arr[2]==str(message.chat.id)):
            msg=arr[0]
            if(msg==""):
                print("no message")
            else:
                await message.reply(msg)
            stage=2
        else:
            await message.reply("Bot is being used by other user")
    else:
        await message.reply("Password please :)")     


@dp.message_handler(commands=['data'])
async def get_data(message : types.message):

    if(functions.CheckWhiteList(message.chat.id)):
        data=open("fulldata.txt","r")
        arr=data.readlines()
        await message.reply('\n'.join(arr))
        #await bot.send_document(message.chat.id,data)
   

@dp.message_handler()
async def noCommand(message : types.message):
    global stage 

    if(stage==0):
        passwordCheck=functions.PasswordCheck(message)
        if(passwordCheck==0):   
            await message.reply("True password /msg")
            stage=1
        else:
            if(passwordCheck==1):
                await message.reply("Wrong password try again")
            if(passwordCheck==2):
                await message.reply("Already used id")
    if(stage==2):
        await message.reply("New Password")
        await message.reply(functions.NewMessage(message))
        stage=0



async def Message(msg):
    await bot.send_message(msg)


executor.start_polling(dp, skip_updates=False)