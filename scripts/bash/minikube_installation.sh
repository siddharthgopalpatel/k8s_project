#!/bin/bash

echo "****************************"
echo "********Updating************"
echo "****************************"
sleep 2
sudo apt-get update

echo "****************************"
echo "*********Upgrading**********"
echo "****************************"
sleep 2
sudo apt-get upgrade -y

echo "****************************"
echo "*******Installing Docker****"
echo "****************************"
sleep 2
sudo apt -y install docker.io

echo "****************************"
echo "*******Installing Kubectl***"
echo "****************************"
sleep 2
sudo curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && chmod +x ./kubectl && sudo mv ./kubectl /usr/local/bin/kubectl

echo "****************************"
echo "******Installing Minikube***"
echo "****************************"
sleep 2
sudo curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/

echo "****************************"
echo "****Installing Conntrack****"
echo "****************************"
sleep 2
sudo apt install conntrack

echo "****************************"
echo "*******Start Minikube*******"
echo "****************************"
sleep 2
sudo minikube start --vm-driver=none

echo "****************************"
echo "*******Minikube Status******"
echo "****************************"
sleep 2
sudo minikube status

echo "****************************"
echo "*******Kubectl Version******"
echo "****************************"
sleep 2
sudo kubectl version

echo "****************************"
echo "*******Getting node*********"
echo "****************************"
sleep 2
sudo kubectl get nodes

echo "****************************"
echo "***Setting up for testuser**"
echo "****************************"
sleep 2
echo 'ubuntu:sidd123' | chpasswd
mkdir -p /home/ubuntu/.kube
sudo cp -i /etc/kubernetes/admin.conf /home/ubuntu/.kube/config
sudo chown -R ubuntu:ubuntu /home/ubuntu/.kube
su - ubuntu
kubectl get nodes
