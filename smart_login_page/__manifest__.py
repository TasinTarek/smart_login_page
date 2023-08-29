# -*- coding: utf-8 -*-
{
    'name': "Smart Login",

    'summary': """
        Smart login page for odoo v16""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo Glow",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','web','website'],
    'data': [
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            'smart_login_page/static/src/css/login.css',
        ],
        'web.assets_common': [
        ],
    },
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
    'contributors': [
        'Tasin Tarek',
    ],
}
