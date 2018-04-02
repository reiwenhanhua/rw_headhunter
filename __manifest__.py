# -*- coding: utf-8 -*-
{
    'name': "RW Mod - Headhunter",

    'summary': """
        Module - 101
    """,

    'description': """
        Headhunter Management
    """,

    'author': "RuiWenHanHua",
    'website': "http://www.ruiwenhanhua.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'ReiWen',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'mail',
                'test_impex',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/baseattribute.xml',
        'views/basemore.xml',
        'views/match.xml',
        'views/job.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}