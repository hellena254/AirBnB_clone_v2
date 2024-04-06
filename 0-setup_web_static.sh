#!/usr/bin/env bash
# prepare the web servers
# sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

# create the folders
sudo mkdir -p /data/ 
sudo mkdir -p /data/web_static/ 
sudo mkdir -p /data/web_static/releases/ 
sudo mkdir -p /data/web_static/releases/test 
sudo mkdir -p /data/web_static/shared

# fake html file
sudo echo "<html>
 <head></head>
 <body>Testing my Configuration</body>
 </html>" | sudo tee /data/web_static/releases/test/index.html

# symbolic link liked to the below folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart for the effects to take place
sudo service nginx start
