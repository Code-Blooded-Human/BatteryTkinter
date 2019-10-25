import tkinter
import os
import time

#Through that function we are gatting status of bettary and also the bettry percentage
#Here we are using os module to use bash commands
def getBat():
	status = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep state | awk '{print $2}'").read()	
	precentage= os.system("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | awk '{print $2}' | sed 's/%//g'")
	percentage = os.popen("upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | awk '{print $2}' | sed 's/%//g'").read()	
	return int(percentage),status 

#this is basiclly a ui height like we have some space in between the battery design the ractangle
#so we are fillig it with some red,yellow and green
#its depandent on the bettarys percentage
def height(bat):

	if bat <= 15 and bat >0 :
		color="red"
	elif bat > 15 and bat < 79:
		color = "yellow"
	else:
		color = "green"


	return int( 215 - ( bat * 130)/100), color
 









x,y=getBat()
h,c=height(x)

print(y)





top = tkinter.Tk()

C = tkinter.Canvas(top, bg="black", height=250, width=250)

coord = 10, 50, 240, 210

left = C.create_polygon(75, 70,85,70, 85, 220,75,220, fill="white")
down = C.create_polygon(75, 220, 75,230, 175,230,175,220, fill="white")
right =C.create_polygon(165,70,175,70,175,220,165,220, fill="white")
topb = C.create_polygon(75, 70,175,70,175,80, 75,80,fill="white")
topbox = C.create_polygon(105,50,145,50,145,70,105,70, fill="white")

bat = C.create_polygon(90,h,160,h,160,215,90,215, fill=c)
C.pack()
#this loop frequently checking battery status
while True:
	a,s=getBat()
	print(s[0])
	if s[0] == "c" :
		C.delete(bat)
		C.update()
		h,c=height(int(33))
		bat = C.create_polygon(90,h,160,h,160,215,90,215, fill="red")
		C.update()	
		time.sleep(1)
		C.delete(bat)
		C.update()
		h,c=height(int(70))
		bat = C.create_polygon(90,h,160,h,160,215,90,215, fill="yellow")
		C.update()
		time.sleep(1)		
		C.delete(bat)
		C.update()
		h,c=height(int(100))
		bat = C.create_polygon(90,h,160,h,160,215,90,215, fill="green")
		C.update()
		time.sleep(1)		
		C.delete(bat)
		C.update()
			
			
	else:	
		h,c=height(a)
		bat = C.create_polygon(90,h,160,h,160,215,90,215, fill=c)
		C.update()	
		time.sleep(1)
		C.delete(bat)

top.mainloop()

