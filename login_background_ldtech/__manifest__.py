# -*- encoding: utf-8 -*-
{
    'name': 'Odoo Login Page Background',
    'summary': 'The new configurable Odoo Web Login Screen',
    'version': '17.0.1.0',  # Updated format
    'category': 'Website',
    'author': 'Livedigital Technologies Private Limited',
    'company': 'Livedigital Technologies Private Limited',
    'maintainer': 'Livedigital Technologies Private Limited',
    'website': 'https://ldtech.in',
    'license': 'LGPL-3',
    'depends': ['base', 'base_setup', 'web', 'auth_signup'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/login_image.xml',
        'templates/assets.xml',
        'templates/left_login_template.xml',
        'templates/right_login_template.xml',
        'templates/middle_login_template.xml',
    ],
    'qweb': [
        # Include any QWeb templates here if needed
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
}
