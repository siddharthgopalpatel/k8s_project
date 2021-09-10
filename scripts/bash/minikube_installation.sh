#!/bin/bash
sudo apt-get update
sudo apt-get upgrade -y
sudo apt -y install docker.io
sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectl
sudo curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
sudo apt install conntrack
sudo minikube start --vm-driver=none
sudo minikube status
sudo kubectl version
sudo kubectl get nodes
