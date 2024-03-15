# Create directory if not exists
mkdir -p bd-a1/service-result
echo "enter id: "

read id

# Copy output files from the container to local machine
docker cp $id:/home/doc-bd-a1/results bd-a1/service-result/

# Stop the container
docker stop $id