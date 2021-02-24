# Building 
docker network create icdar
docker build -t timer ./timer --rm
docker build -t algorithm ./torch --rm
docker build -t evaluation ./evaluation --rm

# Testing
GPU_ID=1
docker run -d --rm --network icdar --name timer --gpus device=$GPU_ID -v $(pwd)/utilization:/utilization timer && 
docker run --rm --network icdar --gpus device=$GPU_ID -v $(pwd)/output:/output -v $(pwd)/data:/data algorithm && 
docker run --rm --network icdar -v $(pwd)/utilization:/utilization -v $(pwd)/output:/output evaluation -g gt.json -s /output/result.json -t 3.2