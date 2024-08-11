{
    'name': 'Custom Font Integration',
    'description': 'Module to integrate custom fonts into Odoo backend and website.',
    'version': '1.0',
    'author': 'author',
    'website': 'thesucess-erp.net',
    'depends': ['base', 'web', 'website'],
    'application': True,
    'data': [
        'views/custom_menu_actions.xml',
        'security/ir.model.access.csv',
        'views/custom_menu.xml',
        'views/custom_font_views.xml',

    ],

    'assets': {
        'web.assets_frontend': [
            'custom_font_integrationn/static/fonts/VisbyCF-MediumOblique.woff',
            'custom_font_integrationn/static/src/css/custom_font_website.css',
        ],
        'web.assets_backend': [
            'custom_font_integrationn/static/fonts/VisbyCF-MediumOblique.woff',
            'custom_font_integrationn/static/src/css/custom_font_backend.css',
        ],
        'web.assets_qweb': [
            'web.assets_frontend',
        ],
    },

}
