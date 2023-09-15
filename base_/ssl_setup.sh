#!/bin/bash

#--------------------------------------------------------------MAKE SURE DON'T FORGOT GIVE PERMISSION FOR THIS FILE FIRST ----------------------------#
# chmod +x scriptname.sh
# ./scriptname.sh your_domain.com



domain=$1

# # Step B1: Install certbot if not installed
# sudo apt update
# sudo apt install certbot python3-certbot-nginx
# #Step B1.2: Check if this domain already have
# Step B2: Obtain SSL certificate for the domain
sudo certbot certonly --nginx -d "$domain"

# Check if certbot command failed
if [ $? -ne 0 ]; then
    echo "Failed to obtain SSL certificate. Exiting."
    exit 1
fi


# Step B3: Create Nginx configuration file
config_file="/etc/nginx/sites-available/$domain"
echo "
server {
    listen 80;
    server_name $domain www.$domain;
    return 301 https://\$host\$request_uri;
}

server {
    listen 443 ssl;
    server_name $domain www.$domain;

    ssl_certificate /etc/letsencrypt/live/$domain/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/$domain/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8070;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_redirect off;
    }
}
" | sudo tee "$config_file" > /dev/null

# Step B4: Create a symbolic link to sites-enabled
sudo ln -s "$config_file" "/etc/nginx/sites-enabled/"

# # Step B5: Check Nginx configuration syntax
# sudo nginx -t

# # If the output shows 0.0.0.0 error, edit the default config
# if [ $? -ne 0 ]; then
#     sudo nano /etc/nginx/sites-available/default
# fi

# Step B6: Restart Nginx
sudo systemctl restart nginx

# Step B7: Access Odoo using the newly configured domain
echo "Xong SSL."

#để xóa các cấu hình không còn cần thiết
# sudo rm /etc/nginx/sites-available/$domain
# sudo rm /etc/nginx/sites-enabled/$domain
# sudo certbot delete --cert-name $domain
# sudo systemctl restart nginx
