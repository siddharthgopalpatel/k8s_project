ps -ef | grep test.py | grep -v grep | awk {'print $2'} | xargs kill -9
cp /home/sidd/k8s_project/manifest/tools/log_pod.txt /home/sidd/k8s_project/manifest/tools/first.txt
#cp /home/sidd/k8s_project/manifest/tools/log_job.txt /home/sidd/k8s_project/manifest/tools/first1.txt
rm -rf /home/sidd/k8s_project/manifest/tools/log_pod.txt
#rm -rf /home/sidd/k8s_project/manifest/tools/log_job.txt

