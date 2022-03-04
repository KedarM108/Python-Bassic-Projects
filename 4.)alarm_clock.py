import datetime
from playsound import playsound

alarmH = int(input("Enter hour :"))
alarmM = int(input("Enter minute :"))
alarmAm = input("am / pm")

if alarmAm == "pm":
    alarmH += 12

while True:
    if alarmH==datetime.datetime.now().hour and alarmM==datetime.datetime.now().minute:
        print("Playing... ")
        playsound("https://www.bensound.com/bensound-music/bensound-ukulele.mp3")
        break