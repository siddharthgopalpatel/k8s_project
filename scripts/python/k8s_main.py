import minikube_installation

def maincode():
    print('''Press 1 to install minikube
    press any other key to exit''')
    input1 = int(input())
    if (input1 == 1):
        minikube_installation.minikube_installation()
    else:
        print("Wrong input")

