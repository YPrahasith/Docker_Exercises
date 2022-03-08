# Docker_Exercises
Simple docker exercises to build docker images and learning about container volumes. 

### Building Docker Image
To build the docker image, run the below command in the working directory :
docker build -t <image-name>:1.0 .

### Docker Volumes
To create a volume in the container and map that to the host system, you can either mount the host filesystem onto the container or you can specify the volume in the docker compose.

For mounting it, we must follow the below steps :
docker run -d \
  --name <some-name> \
  --mount source=<volume-name>,target=<destination-address> \
  nginx:latest

example :
docker run -d \
  --name pyserver \
  --mount source=demoVol,target= /Docker_Assgn \
  nginx:latest

In the other method, we'll just need to run the below command from the working directory and it'll execute the pyserver.yaml file :
docker-compose up