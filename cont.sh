docker run -d --privileged --network host -v /:/host -p 5000:5000 resource-insight:v1 --name resource-insight
docker run -d --privileged -p 5000:5000 --name resource-insight -v /:/host 95osama123/resource-insight:v1 

docker run -d --privileged --network host --name resource-insight -v /:/host 95osama123/resource-insight:v1 
