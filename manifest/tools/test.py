import subprocess

def ssh_master():
    global a,b,c
    a = subprocess.check_output("kubectl get pods -n nidhins 2>/dev/null", shell=True,universal_newlines=True)
    b = subprocess.check_output("date | awk {'print $5'}", shell=True,universal_newlines=True)
    #c = subprocess.check_output("kubectl rollout status deployment mydeploy -n nidhins 2>/dev/null", shell=True,universal_newlines=True)

def write_file_pods():
    f = open("log_pod.txt", "a")
    f.write("*************************************\n")
    f.write(b)
    f.write("*************************************\n")
    f.write(a)
    f.write("*************************************\n")
    f.close()

def write_file_jobs():
    f = open("log_job.txt", "a")
    f.write("*************************************\n")
    f.write(b)
    f.write("*************************************\n")
    f.write(c)
    f.write("*************************************\n")
    f.close()


while (True):
    ssh_master()
    write_file_pods()
    #write_file_jobs()

