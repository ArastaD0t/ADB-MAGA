#! /bin/bash

pass='fF:8E8WF:EW844fd8?:'

if [ "$1" = "--h" ]; then
echo "MassAccountGeneratorADB"
echo ""
echo " --h   For help"
#echo " --n   For namelist.txt"
echo " --p   For password (min 8 lenght)"
else

if [ "$1" = "--p" ]; then
	if [ "$2" != "" ]; then
		pass="$2"
	else
		 ./MAGA.sh --h
	fi
else
	pass='fF:8E8WF:EW844fd8?:'
fi
echo $pass
fname="shuf -n 1 fname.txt"
lname="shuf -n 1 lname.txt"
year="shuf -n 1 year.txt"
day='09'

adb shell am start -n com.android.settings/.accounts.AddAccountSettings
sleep 1
./adbTouch.sh Google
#echo TYPE PASSWORD IF ON SCREEEN REQUESTED
#sleep 9
sleep 3
./adbTouch.sh 'Vytvořit účet'
sleep 1
adb shell input tap 200 850 ##personal type
sleep 2
adb shell input tap 150 500 ##name
adb shell input text $($fname) keyboard
adb shell input keyevent 66
adb shell input text $($lname) keyboard
./adbTouch.sh 'Další'
sleep 1
adb shell input tap 140 500 ##den
sleep 2
adb shell input text $day keyboard
sleep 2
adb shell input tap 345 500 ##měsíc
sleep 2
adb shell input tap 345 500 ##duben
sleep 2
adb shell input tap 500 500 ##měsíc
sleep 2 
adb shell input text $($year) keyboard
sleep 2
adb shell input tap 400 640
sleep 2
adb shell input tap 400 640 #gender male
sleep 2
./adbTouch.sh 'Další'
./adbTouchRadio.sh
./adbTouch.sh 'Další'

#adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml
#grep -q "vlastní" /tmp/view.xml; test $? -eq 0 && echo "Used" & ./adbTouchRadio.sh & sleep 3 & ./fgmail.sh &  sleep 3 & ./adbTouch.sh Další && echo final || echo "Free"


EMAIL=$(cat /tmp/gmail.var)
echo GMAIL: $EMAIL
echo PASS: $pass
sleep 3
adb shell input text $pass keyboard
echo password entered
sleep 1
adb shell input keyevent 66
echo Pressed Enter

adb shell input swipe 500 1000 300 300 #scroll down
echo scroll
adb shell input swipe 500 1000 300 300 #scroll down
echo scroll

./adbTouch.sh 'Přeskočit'
echo skip
sleep 3
./adbTouch.sh 'Další'
echo next
sleep 1
./adbTouchRadio.sh
echo touch Radio
sleep 3
./adbTouch.sh 'Další'
echo next
sleep 1
adb shell input swipe 500 1000 300 300
echo swipe
adb shell input swipe 500 1000 300 300
echo swipe
sleep 1
adb shell input swipe 500 1000 300 300
echo swipe
sleep 1
adb shell input swipe 500 1000 300 300
sleep 1

./adbTouch.sh 'Potvrdit'
echo accept
echo $EMAIL $pass  >> $(date +%T)-$(date +%F).gmail
echo ######################
echo $EMAIL
echo $pass
echo ######################

adb shell input swipe 500 1000 300 300
echo swipe
sleep 1
adb shell input swipe 500 1000 300 300
sleep 1
./adbTouch.sh 'Souhlasím'

rm -r /tmp/view.xml
fi
