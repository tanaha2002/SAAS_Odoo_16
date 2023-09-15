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

#--------------------method 1: read from record id--------------------
    # field_name = 'x_subsystem_want_receive'
    # record_name = 'a'  # Replace with the actual name of the record you created

    # # Get the ID of the record with the specified name
    # record_id = client.model('crm.lead').search([('name', '=', record_name)], limit=1)

    # #print all lead data from this record  
    # print(client.model('crm.lead').read(record_id, ['name', 'contact_name', 'phone', 'email_from', 'partner_name', 'website', 'description', 'x_contact_via', 'x_subsystem_want_to_receive', 'x_company_size']))
#--------------------method 2: read all available options of fields--------------------
# go to the config (Cấu hình) in CRM -> lead -> subsystem (Phân hệ) -> click on the name of options -> view metadata -> get the id of the option
# id = 1: Thúc đẩy kinh doanh
# id = 4: Nâng cao hiệu suất làm việc
# id = 5: Tư vấn tổng thể về giải pháp B-ERP

    if type_db == 'CRM-BASE':
        subsystem = 1
    elif type_db == 'PM-BASE':
        subsystem = 4
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

