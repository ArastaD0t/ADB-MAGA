from time import sleep
#from PIL import Image
import random
import sys
import os

##Random Sleep##
rsleep= random.randint(0, 6)
####

######Colors&Formats#############
yb= "\033[1;33;40m" ##YellowBold
wb= "\033[1;37;40m" ##WhiteBold
cb= "\033[1;32;40m" ##CyanBold
y= "\033[0;33;40m"  ##Yellow
c= "\033[0;32;40m"  ##Cyan
r= "\033[0;31;40m"  ##Red
###

##adb Touch Button##
#BUTTON="DALŠÍ"
#adbTouch= os.system("./adbTouch.sh %s"% (BUTTON))





#########################
#  GOOGLE ACCOUNT       #
#########################
os.system("adb shell am start -n com.android.settings/.accounts.AddAccountSettings") ##OPEN ACCOUNTS SETTINGS
print("%s[%si%s]%s Accounts settings opened%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input tap 250 625") ##SELECT GOOGLE ACCOUNT ADD
print("%s[%si%s]%s Google account selected%s"% (wb,cb,wb,c,r))
sleep(9)
os.system("adb shell input tap 150 1100") ##CREATE
print("%s[%si%s]%s Create Google account%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input tap 200 1200") ##FOR ME
print("%s[%si%s]%s Account type set Personal%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input tap 500 800") ##FIRST NAME
print("%s[%si%s]%s Select First Name%s"% (wb,cb,wb,c,r))
sleep(rsleep)

FNAME= "Alan"

os.system("adb shell input text %s keyboard"% (FNAME))
print("%s[%si%s]%s First name set to %s%s%s"% (wb,cb,wb,c,y,FNAME,r))
sleep(rsleep)
os.system("adb shell input tap 900 900") ##NEXT
print("%s[%si%s]%s Touch Next...%s"% (wb,cb,wb,c,r))
print("%s[%si%s]%s Select Last Name%s"% (wb,cb,wb,c,r))
sleep(rsleep)

LNAME= "Bigman"

os.system("adb shell input text %s keyboard"% (LNAME))
print("%s[%si%s]%s Last name set to %s%s%s"% (wb,cb,wb,c,y,LNAME,r))
sleep(rsleep)
os.system("adb shell input tap 900 900") ##NEXT  
print("%s[%si%s]%s Touch Next...%s"% (wb,cb,wb,c,r))
sleep(3)
os.system("adb shell input tap 100 700") ##SELECT DAY 
print("%s[%si%s]%s Select Day%s"% (wb,cb,wb,c,r))

sleep(rsleep)

day= "01"

os.system("adb shell input text %s keyboard"% (day))
print("%s[%si%s]%s Day set to %s%s%s"% (wb,cb,wb,c,y,day,r))
sleep(rsleep)
os.system("adb shell input tap 400 700") ##SELECT MONTH
print("%s[%si%s]%s Select Month%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input tap 400 150") ##SET MONTH (01 150,02 300,03 500,04 700,... EVERY NEXT MONTH +200) 
print("%s[%si%s]%s Month set to default (%sJanuary%s)%s"% (wb,cb,wb,c,y,c,r))
sleep(rsleep)
os.system("adb shell input tap 900 700") ##SELECT YEAR
print("%s[%si%s]%s Select Year%s"% (wb,cb,wb,c,r))

year= "1995"

os.system("adb shell input text %s keyboard"% (year))
print("%s[%si%s]%s Year set to %s%s%s"% (wb,cb,wb,c,y,year,r))
sleep(rsleep)
os.system("adb shell input tap 700 900") ##SELECT GENDER
print("%s[%si%s]%s Select Gender%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input tap 700 900") ##SET GENDER F=700 M=900 N=1100 C=1300
print("%s[%si%s]%s Set Gender to default (%sman%s)%s"% (wb,cb,wb,c,y,c,r))
sleep(rsleep)
os.system("adb shell input tap 900 1800") ##NEXT
print("%s[%si%s]%s Touch Next...%s"% (wb,cb,wb,c,r))
sleep(rsleep)
os.system("adb shell input text '%s'.'%s''%s' keyboard"% (FNAME,LNAME,year))
print("%s[%si%s]%s Username set to %s%s.%s%s%s"% (wb,cb,wb,c,y,FNAME,LNAME,year,r))
os.system("adb shell input tap 900 900") ##NEXT
print("%s[%si%s]%s Touch Next...%s"% (wb,cb,wb,c,r))
os.system("rm /tmp/view.xml") ##REMOVE OLD TMP
os.system("adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml") ##REQUESTING USERNAME USAGE STATE...
sleep(3)


with open("/tmp/view.xml") as f:
	for line in f:
		if "vlastní" in line:
		   print("%s[%sW%s]%s Username %s%s.%s%s %sis already used!%s"% (wb,yb,wb,c,y,FNAME,LNAME,year,c,r))
		   adbTouch= os.system("./adbTouchRadio.sh") #select first alternative email
		   GMAIL= os.system("./fgmail.sh")
		   BUTTON="DALŠÍ"
		   adbTouch= os.system("./adbTouch.sh %s"% (BUTTON)) #NEST
		else:
	            #UNAME= f"{FNAME}.{LNAME}{year}"
		    #GMAIL= f"{FNAME}.{LNAME}{year}@gmail.com"
		   print("%s[%si%s]%s Username is free%s"% (wb,cb,wb,c,r))

PASS= "fF:8E8WF:EW844fd8?:"
os.system("adb shell input text %s keyboard"% (PASS))

BUTTON="DALŠÍ"
adbTouch= os.system("./adbTouch.sh %s"% (BUTTON)) #NEST

os.system("adb shell input swipe 500 1000 300 300 ") #scroll down
os.system("adb shell input swipe 500 1000 300 300 ") #scroll down

BUTTON="Přeskočit"
adbTouch= os.system("./adbTouch.sh %s"% (BUTTON)) #skip tell number

BUTTON="DALŠÍ"
adbTouch= os.system("./adbTouch.sh %s"% (BUTTON)) #NEXT


#os.system("adb shell input tap 850 950")

#os.system("cat /tmp/view.xml|egrep -o "[^[:space:]]+@[^[:space:]]+" | tr -d "<>"| cut -d '=' -f 2 | sed 's/"//g'")






#print("%s[%sA%s]%s Check image or screen for unused username....%s"% (wb,yb,wb,c,r))


#os.system("adb shell input swipe 250 800 250 400 300 ") ##SCROLL DOWN
#os.system("adb exec-out screencap -p > screen.png")
#sleep(5)
#im = Image.open(r"screen.png") 
#im.show()
#sleep(5)
#os.system("rm screen.png")


sleep(999)
sleep(999)
sleep(999)

sleep(rsleep)
os.system("adb shell input tap 900 1000") ##NEXT  
print("[i] Touch Next...")



###


########################
#     ACCOUNT INFO     #
########################
#ANAME= print("%s %s"% (FNAME,LNAME))
#UNAME= print("%s.%s%s"% (FNAME,LNAME,year))
#GMAIL= print("%s.%s%s@gmail.com"% (FNAME,LNAME,year))
#PASS=  print("fF:8E8WF:EW844fd8?:")

ANAME= f"{FNAME} {LNAME}"

PASS= "fF:8E8WF:EW844fd8?:"

print("")
print("")
print("")
print("")


print("###############################")
print("#   Google Account Details    #")
print("###############################")
BUTTON="DALŠÍ"
adbTouch= os.system("./adbTouch.sh %s"% (BUTTON)) #NEST


print("# Full Name :%s"% (ANAME))
print("# User Name :%s"% (UNAME))
print("# Adress  :%s"% (GMAIL))
print("# Password :%s"% (PASS))
print("###############################")








sleep(999)
sleep(999)
sleep(999)




#########################
#   FACEBOOK ACCOUNT    #
#########################
os.system("adb shell am start -n com.facebook.katana/com.facebook.katana.LoginActivity")
os.system("adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml")
os.system("adb shell input tap 500 1750")
os.system("adb shell input tap 500 1350")
os.system("adb shell input tap 500 1350")
##FISRT.NAME##
os.system("adb shell input tap 250 750")
os.system("adb shell input text +fname keyboard")

