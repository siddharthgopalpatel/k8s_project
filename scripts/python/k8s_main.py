import minikube_installation
import minikube_status

def maincode():
    print('''Press 1 to install minikube
Press 2 to check minikube status
press any other key to exit''')
    input1 = int(input())
    if (input1 == 1):
        minikube_installation.minikube_install()
    elif (input1 == 2):
        minikube_status.status()
    else:
        print("Wrong input")

maincode()
