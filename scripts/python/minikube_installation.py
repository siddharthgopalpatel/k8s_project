import subprocess
import time
import minikube_status

def countdown():
        t = 5
        while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print("*****Waiting Time Countdown for 5 seconds ==> ",timer, "*****",end="\r")
                time.sleep(1)
                t -= 1

        print('Times up !!!')

def minikube_install():
    print("""****************************"
********Updating************
****************************""")
    subprocess.call("sudo apt-get update", shell=True)
    countdown()

    print ("""****************************
*********Upgrading**********
****************************""")
    subprocess.call("sudo apt-get upgrade -y", shell=True)
    countdown()

    print ("""****************************
*******Installing Docker****
****************************""")
    subprocess.call("sudo apt -y install docker.io", shell=True)
    countdown()

    print ("""****************************
*******Installing Kubectl********
****************************""")
    subprocess.call("sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectl",  shell=True)
    countdown()

    print ("""****************************
******Installing Minikube***
****************************""")
    subprocess.call("sudo curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/", shell=True)
    countdown()

    print("""****************************
****Installing Conntrack****
****************************""")
    subprocess.call("sudo apt install conntrack", shell=True)
    countdown()

    print ("""****************************
*******Start Minikube*******
****************************""")
    subprocess.call("sudo minikube start --vm-driver=none", shell=True)
    countdown()

    print("""****************************
*******Minikube Status******
****************************""")
    subprocess.call("sudo minikube status", shell=True)
    countdown()

    print("""****************************
*******Kubectl Version******
****************************""")
    subprocess.call("sudo kubectl version", shell=True)
    countdown()

    print("""****************************
*******Getting node*********
****************************""")
    subprocess.call("sudo kubectl get nodes", shell=True)
    countdown()

    print("""****************************
***Setting up for testuser**
****************************""")
    subprocess.call("echo 'ubuntu:sidd123' | chpasswd", shell=True)
    subprocess.call("mkdir -p /home/ubuntu/.kube", shell=True)
    subprocess.call("sudo cp -i /etc/kubernetes/admin.conf /home/ubuntu/.kube/config", shell=True)
    subprocess.call("sudo chown -R ubuntu:ubuntu /home/ubuntu/.kube", shell=True)
    countdown()
    minikube_status.status()
    subprocess.call("su - ubuntu", shell=True)
