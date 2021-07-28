# -*- coding: utf-8 -*-
{
    'name': "ESI_Compet",

    'summary': """pour les competition xD""",

    'description': """
        ESI_Compet module for competition            
    """,

    'author': "ESI",
    'website': "http://www.mesrs.dz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/esicompet.xml',
        'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
