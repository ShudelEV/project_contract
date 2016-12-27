# -*- coding: utf-8 -*-

{
    'name': 'Project Contract',
    'version': '1.1',
    'author': 'ShEV',
    'category': 'Project Management',
    'description': """
Project Contract
================
""",
    'website': '',
    'depends': [
        'project',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/project_contract_view.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': True,
}
