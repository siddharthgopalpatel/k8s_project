import subprocess
import datetime

def time_fun():
    x = datetime.datetime.now()

    h = str(x.hour)
    m = str(x.minute)
    s =  str(x.second)
    time = ""+ h +":"+ m +":"+ s +""

    return time

try:
    a1 = subprocess.check_output("ssh nidhi@gopalan ls -ltr /home/epatesi/practice/python_practice/test/sample.txt", shell=True)


    if (a1):
        f = open("output.txt", "a")
        a = f.write(""+ time_fun() +" file present\n")
        f.close()

except:
        f = open("output.txt", "a")
        a = f.write(""+ time_fun() +" file absent\n")
        f.close()
