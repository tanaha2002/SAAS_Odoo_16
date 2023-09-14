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
    url = cf.url_base
    client = erppeek.Client(server=url)

    # login with 1st database
    db_name = client.db.list()[0]
    user = 'bbsw_crm'
    password = 'bbsw123'

    client = erppeek.Client(server=url, db=db_name, user=user, password=password)
    #get company id
    #cids
    company_id = 2  
    #get data from config file
    config = configparser.ConfigParser()
    config.read('database_info.ini')
    #create a lead data info about contact name, phone, email, company, website, description
    website = 'https://' + config['DATABASE']['db_name'] + 'berp.vn'
    type_db = config['DATABASE']['type_of_db']
    if type_db == 'CRM-BASE':
        subsystem = 1
    elif type_db == 'PM-BASE':
        subsystem = 2
    lead_data = {
        'name': 'Tạo database thành công',
        'contact_name': config['DATABASE']['name_user'],
        'phone': config['DATABASE']['phone'],
        'email_from': config['DATABASE']['login_name'],
        'partner_name': config['DATABASE']['company_name'],
        'website': website,
        'description': config['DATABASE']['description'],
        'x_contact_via': config['DATABASE']['support_type'], 
        'x_subsystem_want_to_receive': subsystem, 
        'x_company_size': config['DATABASE']['company_size'],


    }
    #get current user id
    user_id = client.model('res.users').search([('login', '=', 'admin')])

    client.write('res.users', user_id, {'company_id': company_id})
    lead_id = client.create('crm.lead', lead_data)
    print('create lead success')
except subprocess.CalledProcessError as e:
    # print(f"Error creating database: {e.output}")
    print('create lead fail')

