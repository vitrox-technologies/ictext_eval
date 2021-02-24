# Building 
docker build -t evaluation ./evaluation --rm

# Testing
docker run --rm -v $(pwd)/output:/output evaluation -g gt.json -s /output/result.json -t 1