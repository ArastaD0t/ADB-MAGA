import os
import sys
print("$(os.system("whoami"))")
#print("$(os.system("cat /tmp/view.xml|egrep -o "[^[:space:]]+@[^[:space:]]+" | tr -d "<>"| cut -d '=' -f 2 | sed 's/"//g' |sed -e '$ d'|sed -e '$ d'|sed -e '$ d'"))")
