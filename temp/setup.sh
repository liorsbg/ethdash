# install gcloud
# init gcloud

# Create node
gcloud beta compute --project "ethdash-42" instances create "instance-1" --zone "europe-west3-a" --machine-type "n1-standard-2" --subnet "default" --maintenance-policy "MIGRATE" --service-account "850995022360-compute@developer.gserviceaccount.com" --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring.write","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --min-cpu-platform "Automatic" --tags "http-server","https-server" --image "ubuntu-1604-xenial-v20180306" --image-project "ubuntu-os-cloud" --boot-disk-size "100" --boot-disk-type "pd-standard" --boot-disk-device-name "instance-1"

# Or bigger node
gcloud beta compute --project "ethdash-42" instances create "instance-2" --zone "europe-west3-a" --machine-type "n1-standard-4" --subnet "default" --maintenance-policy "MIGRATE" --service-account "850995022360-compute@developer.gserviceaccount.com" --scopes "https://www.googleapis.com/auth/devstorage.read_only","https://www.googleapis.com/auth/logging.write","https://www.googleapis.com/auth/monitoring.write","https://www.googleapis.com/auth/servicecontrol","https://www.googleapis.com/auth/service.management.readonly","https://www.googleapis.com/auth/trace.append" --min-cpu-platform "Automatic" --tags "http-server","https-server" --image "ubuntu-1604-xenial-v20180306" --image-project "ubuntu-os-cloud" --boot-disk-size "100" --boot-disk-type "pd-ssd" --boot-disk-device-name "instance-2"
gcloud compute --project=ethdash-42 firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server
gcloud compute --project=ethdash-42 firewall-rules create default-allow-https --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:443 --source-ranges=0.0.0.0/0 --target-tags=https-server


# Log into node
gcloud compute ssh instance-1

# Get docker
curl -fsSL https://get.docker.com -o get-docker.sh

# Install dokcer
sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker liorsabag

# Run geth node docker
docker run --name geth -it -p 30303:30303 -p 8545:8545 -v /home/liorsabag/geth1:/root ethereum/client-go --rpc --rpcaddr "0.0.0.0" --cache 4096

# Run linked python3.6 container
docker run --name api -it -v /home/liorsabag/geth1:/root/geth1 python:3.6 bash

# TODO: build from Dockerfile with web3 ipython flask?