import erppeek
import configparser
import os
import time
import subprocess
from xmlrpc import client
import sys
sys.path.append('/opt/odoo/odoo-server/custom_addons/registry_account')
import config as cf

try:
    # # Đọc thông tin từ tệp
    config = configparser.ConfigParser()
    config.read('database_info.ini')
    db_name = config['DATABASE']['db_name']
    admin_password = config['DATABASE']['admin_password']
    user_password = config['DATABASE']['user_password']
    login = config['DATABASE']['login_name']
    name_user = config['DATABASE']['name_user']
    db_name_clone = config['DATABASE']['type_of_db']
    #replace with ur base-database info
    base_login = "admin"
    base_passwd = "admin123@"

    # Source Odoo database info
    url = cf.url

    # Target Odoo database info
    base_login = cf.base_login
    base_passwd = cf.base_passwd

    #linux
    shell_script_path =  cf.shell_script_path
    subprocess.check_output([shell_script_path, db_name,db_name_clone, admin_password, url])

    #create a new user in new database
    client = erppeek.Client(server=url, db=db_name, user=base_login, password=base_passwd)
    admin_id = client.model('res.users').search([('login', '=', 'admin')])

    groups_id = client.model('res.users').read([admin_id[0]], ['groups_id'])[0]['groups_id']

    # New user parameters
    new_user_vals = {
        'name': name_user,
        'login': login,
        'password': user_password,
        #give full group id for all module id
        'groups_id': [(6, 0, groups_id)],

    }
    # #create a new user in new database with admin rights
    new_user_id = client.create('res.users', new_user_vals)
    print('create user success')

except subprocess.CalledProcessError as e:
    print('create user fail')



