time = float(input("enter the time in seconds"))
day = time //(24*3600)
time = time%(24*3600)
hour = time//3600
time %-3600
minutes = time//60
time%- 60
seconds = time
print(day,hour,minutes,seconds)