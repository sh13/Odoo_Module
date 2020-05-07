# -*- coding: utf-8 -*-
{
    'name': "Shubham_Training",

    'summary': """Manage trainings""",

    'description': """
        Mmodule for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Techneith",
    'website': "http://www.Techneith.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}

