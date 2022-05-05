file=open("current_info.txt","r")
arr=file.readlines()
print(arr)
arr[0]="kekw"
file=open("current_info.txt","w")
file.writelines(arr)
print(arr)