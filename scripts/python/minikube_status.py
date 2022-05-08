import subprocess

def status():
    print("***************************************************")
    cmd1 = "minikube status | grep -E 'host|kubelet|apiserver'"
    print('command in list format:',cmd1)
    sp = subprocess.check_output(cmd1,shell=True,universal_newlines=True)
    for line in sp.splitlines():
        if "Running" in line.split()[1]:
            print(line.split()[0].rstrip(':'), "is Running")
        else:
            print(line.split()[0].rstrip(':'), 'status is :',line.split()[1])
    print("***************************************************")

    cmd2 = "minikube status | grep 'kubeconfig'"
    print('command in list format:',cmd2)
    sp1 = subprocess.check_output(cmd2,shell=True,universal_newlines=True)
    for line in sp1.splitlines():
        if "Configured" in line.split()[1]:
            print(line.split()[0].rstrip(':'), "is Running")
        else:
            print(line.split()[0].rstrip(':'), 'status is :',line.split()[1])
    print("***************************************************")

    cmd3 = "kubectl get pods -n kube-system | sed '1d'"
    print('command in list format:',cmd3)
    sp2 = subprocess.check_output(cmd3,shell=True,universal_newlines=True)
    for line in sp2.splitlines():
        if "Running" in line.split()[2]:
            print(line.split()[0], "Pod is Running")
        else:
            print('FAILED, status is : ',line.split()[2])
    print("***************************************************")

    cmd4 = "kubectl get pods -n kube-system | sed '1d' | wc -l"
    print('command in list format:',cmd4)
    sp3 = subprocess.check_output(cmd4,shell=True,universal_newlines=True)
    if (int(sp3) == 7):
        print("Seven pods are present")
    else:
        print("Pods are missing in Kube-system namespace")
    print("***************************************************")

