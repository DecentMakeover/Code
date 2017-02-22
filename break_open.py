import webbrowser
import time

num = 0
print ('This program started on: '+ time.ctime())
while num <= 2:
    time.sleep(10)
    webbrowser.open('http://www.ribbonfarm.com/')
    num +=1

