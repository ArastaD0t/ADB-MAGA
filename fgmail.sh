cat /tmp/view.xml|egrep -o "[^[:space:]]+@[^[:space:]]+" | tr -d "<>"| cut -d '=' -f 2 | sed 's/"//g'|grep -m1 ""  > /tmp/gmail.var
