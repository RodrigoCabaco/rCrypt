import sys
import base64

msg = sys.argv[2]
str_type = sys.argv[1]
encoded =""
decoded =""

if str_type=="--encode":
    encoded = base64.b64encode(bytes(msg,'utf-8'))
    f = open('encoded','w+')
    f.write(str(encoded).split('b\'')[1].split('\'')[0])
    f.close()
elif str_type =="--decode":
    decoded = base64.b64decode(bytes(msg,'utf-8'))
    f = open('encoded','w+')
    f.write(str(decoded).split('b\'')[1].split('\'')[0])
    f.close()