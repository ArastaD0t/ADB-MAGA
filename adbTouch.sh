
TEXT=$1

adb pull $(adb shell uiautomator dump | grep -oP '[^ ]+.xml') /tmp/view.xml
sleep 1
export TEXT
coords=$(perl -ne 'printf "%d %d\n", ($1+$3)/2, ($2+$4)/2 if /text="$ENV{TEXT}"[^>]*bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"/' /tmp/view.xml)
adb shell input tap $coords
echo $coords
