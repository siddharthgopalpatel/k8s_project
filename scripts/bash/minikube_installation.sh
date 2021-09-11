#!/bin/bash
echo "****************************"
echo "********Updating************"
echo "****************************"
sudo apt-get update

echo "****************************"
echo "*********Upgrading**********"
echo "****************************"
sudo apt-get upgrade -y

echo "****************************"
echo "*******Installing Docker****"
echo "****************************"
sudo apt -y install docker.io

echo "****************************"
echo "*******Installing Kubectl***"
echo "****************************"
sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectl

echo "****************************"
echo "******Installing Minikube***"
echo "****************************"
sudo curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

echo "****************************"
echo "****Installing Conntrack****"
echo "****************************"
sudo apt install conntrack

echo "****************************"
echo "*******Start Minikube*******"
echo "****************************"
sudo minikube start --vm-driver=none

echo "****************************"
echo "*******Minikube Status******"
echo "****************************"
sudo minikube status

echo "****************************"
echo "*******Kubectl Version******"
echo "****************************"
sudo kubectl version

echo "****************************"
echo "*******Getting node*********"
echo "****************************"
sudo kubectl get nodes

echo "****************************"
echo "***Setting up for testuser**"
echo "****************************"
useradd -m sidd
echo 'sidd:sidd123' | chpasswd
mkdir -p /home/sidd/.kube
sudo cp -i /etc/kubernetes/admin.conf /home/sidd/.kube/config
sudo chown sidd:sidd /home/sidd/.kube/config