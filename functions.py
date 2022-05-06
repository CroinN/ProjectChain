import string
import random



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

    File=open("wishes.txt","r")
    arr=File.readlines()
    arr.__iadd__(str(msg.text)+"\n")
    File=open("wishes.txt","w")
    File.writelines(arr)

    return newPassword

def PasswordCheck(msg):
    if(CheckUsers(msg.chat.id)):
        if(CheckWhiteList(msg.chat.id)==False):
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

def CheckUsers(user_id):
    id=str(user_id)+"\n"
    File=open("users.txt","r")
    arr=File.readlines()
    for i in arr:
        if(id==i):
            return True
    return False

def CheckWhiteList(user_id):
    id=str(user_id)+"\n"
    File=open("whitelist.txt","r")
    arr=File.readlines()
    for i in arr:
        if(id==i):
            return True
    return False