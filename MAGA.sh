fname=Hanz
lname=Soloo
year=1972
day=01

adb shell am start -n com.android.settings/.accounts.AddAccountSettings
sleep  9
./adbTouch.sh Google
echo TYPE PASSWORD IF ON SCREEEN REQUESTED
sleep 9
./adbTouch.sh 'Vytvořit účet'
sleep 1
adb shell input tap 200 850 ##personal type
sleep 2
adb shell input tap 150 500 ##name
adb shell input text $fname keyboard
./adbTouch.sh Další
adb shell input text $lname keyboard
./adbTouch.sh Další
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
adb shell input text $year keyboard
sleep 2
adb shell input tap 400 640
sleep 2
adb shell input tap 400 640 #gender male
sleep 2
./adbTouch.sh Další






