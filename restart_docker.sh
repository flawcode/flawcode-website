# get the name of the process
ps_name=$(docker ps | awk '{print $15}' | grep -E "\w+")
echo "name found ", ${ps_name}

# stop it
echo "stopping..."
docker stop ${ps_name}

# delete it
echo "deleting..."
docker rm ${ps_name}

# run new process
echo "starting new process..."
docker run -p 8888:80 -d -v ~/flawcode:/usr/share/nginx/html nginx
