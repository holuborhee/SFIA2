#!/bin/bash/
source /home/jenkins/.profile

sudo chmod 666 /var/run/docker.sock
docker-compose build
sudo docker login
sudo docker push ngww/service1:latest
sudo docker push ngww/service2:latest
sudo docker push ngww/service3:latest
sudo docker push ngww/service4:latest
docker stack deploy --compose-file docker-compose.yaml sfia2
