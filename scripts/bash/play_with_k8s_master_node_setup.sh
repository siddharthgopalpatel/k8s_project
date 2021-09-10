#yum update -y
#yum upgrade -y
echo "************Installing softwares*******************"
yum install vim openssh* net-tools sudo -y
echo "****adding sidd user, making it sudo user, changing sidd and root user password***"
sleep 5
useradd sidd
echo 'sidd:sidd123' | chpasswd
echo 'root:root123' | chpasswd
echo "sidd    ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers
echo "************Running kubeadm init command********************"
sleep 5
kubeadm init --apiserver-advertise-address $(hostname -i) --pod-network-cidr 10.5.0.0/16
echo "************Running for network setup************************"
sleep 5
kubectl apply -f https://raw.githubusercontent.com/cloudnativelabs/kube-router/master/daemonset/kubeadm-kuberouter.yaml
echo "************Running command for sidd user********************"
sleep 5
runuser -l  sidd -c 'mkdir -p $HOME/.kube'
runuser -l  sidd -c 'sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config'
runuser -l  sidd -c 'sudo chown $(id -u):$(id -g) $HOME/.kube/config'
echo "**************Copy followed line and paste on worker node**********"
grep -A 1 'kubeadm join' output.txt
