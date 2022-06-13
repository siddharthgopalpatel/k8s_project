import subprocess

def ssh_master():
    global a
    a = subprocess.check_output("ssh sidd@192.168.1.27 kubectl get pods 2>/dev/null", shell=True,universal_newlines=True)

def write_file():
    f = open("log.txt", "a")
    f.write("*************************************\n")
    f.write(a)
    f.write("*************************************\n")
    f.close()

def read_file():
    f = open("log.txt", "r")
    print(f.read())

while (True):
    ssh_master()
    write_file()
#read_file()
