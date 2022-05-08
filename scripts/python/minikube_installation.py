import subprocess

def minikube_installation():
    print("""****************************"
    ********Updating************
    ****************************""")
    sleep 2
    subprocess.check_output("sudo apt-get update", shell=True)

    print ("""****************************
    "*********Upgrading**********
    ****************************""")
    sleep 2
    subprocess.check_output("sudo apt-get upgrade -y", shell=True)

    print ("""****************************
    *******Installing Docker****
    ****************************""")
    sleep 2
    subprocess.check_output("sudo apt -y install docker.io", shell=True)

    print ("""****************************
    *******Installing Kubectl********
    "****************************""")
    sleep 2
    subprocess.check_output("sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectl",  shell=True)

    print ("""****************************
    ******Installing Minikube***
    ****************************""")
    sleep 2
    subprocess.check_output("sudo curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/", shell=True)

    print("""****************************
    ****Installing Conntrack****
    ****************************""")
    sleep 2
    subprocess.check_output("sudo apt install conntrack", shell=True)

    print ("""****************************
    *******Start Minikube*******
    ****************************""")
    sleep 2
    subprocess.check_output("sudo minikube start --vm-driver=none", shell=True)

    print("""****************************
    *******Minikube Status******
    ****************************""")
    sleep 2
    subprocess.check_output("sudo minikube status", shell=True)

    print("""****************************
    *******Kubectl Version******
    ****************************""")
    sleep 2
    subprocess.check_output("sudo kubectl version", shell=True)

    print("""****************************
    *******Getting node*********
    ****************************""")
    sleep 2
    subprocess.check_output("sudo kubectl get nodes", shell=True)

    print("""****************************
    ***Setting up for testuser**
    ****************************""")
    sleep 2
    subprocess.check_output("echo 'ubuntu:sidd123' | chpasswd", shell=True)
    subprocess.check_output("mkdir -p /home/ubuntu/.kube", shell=True)
    subprocess.check_output("sudo cp -i /etc/kubernetes/admin.conf /home/ubuntu/.kube/config", shell=True)
    subprocess.check_output("sudo chown -R ubuntu:ubuntu /home/ubuntu/.kube", shell=True)
    subprocess.check_output("su - ubuntu", shell=True)
    subprocess.check_output("kubectl get nodes", shell=True)
