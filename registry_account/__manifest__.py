{
    'name': 'Company Registry',
    'version': '1.0',
    'summary': 'Customize the registry page of Odoo',
    'description': 'Custom module to customize the registry page for Odoo',
    'category': 'Website',
    'author': 'Tanaha2002',
    'depends': ['base', 'web'],
    'images': ['static/src/images/CRM.png',
               'static/src/images/Sales.png',
               'static/src/images/Online Chat.png',
               'static/src/images/Booking.png'
               ],
    'data': [
        'views/sign_up_account.xml',
        'views/add_in_login.xml',
        'views/choose_apps_views.xml',
        'views/dang_ky.xml',
        
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'registry_account/static/src/css/select_apps.css',
    #     ]
    # },
    'qweb': ['static/src/xml/select_apps_assets.xml',
             'static/src/xml/sign_up_assets.xml',
             'static/src/xml/registry_assets.xml',],
    'installable': True,



}