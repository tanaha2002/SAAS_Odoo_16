#!/bin/bash

# Define the directory where nginx configuration files are stored
NGINX_CONF_DIR="/etc/nginx/sites-available/"

# Define the directory where symbolic links to enabled sites are stored
NGINX_ENABLED_DIR="/etc/nginx/sites-enabled/"

# Function to remove a site
remove_site() {
    site_name="$1"

    # Check if the site exists in sites-available
    if [ -f "${NGINX_CONF_DIR}${site_name}" ]; then
        # Remove the site from sites-enabled (if it exists there)
        sudo rm -f "${NGINX_ENABLED_DIR}${site_name}"

        # Remove the site from sites-available
        sudo rm -f "${NGINX_CONF_DIR}${site_name}"
        echo "Site '$site_name' removed successfully."
    else
        echo "Site '$site_name' does not exist in sites-available."
    fi
}

# Function to restart nginx
restart_nginx() {
    sudo systemctl restart nginx
    echo "Nginx restarted."
}

# Usage instructions
if [ $# -eq 0 ]; then
    echo "Usage: $0 <site1> <site2> ... <siteN>"
    exit 1
fi

# Iterate through the provided site names and remove them
for site in "$@"
do
    remove_site "$site"
done

# Restart nginx
restart_nginx