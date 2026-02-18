# -*- coding: utf-8 -*-
{
    'author': 'Numériques, Lucas Délèze fork de Auxil HOUESSOU',
    'website': 'https://numeriques.ch',
    'license': 'LGPL-3',
    'depends': ['base', 'portal', 'web', 'mail', 'helpdesk_mgmt'],
    'name': 'Custom Theme Colors',
    'version': '18.0.1.3.0',
    'summary': 'Personnalisation des couleurs Odoo',
    'description': """
        Module pour personnaliser les couleurs de l'interface Odoo.
        Change la couleur principale violette pour votre couleur préférée.
    """,
    'category': 'Hidden',
    'data': [
        'data/color_config.xml',
        'views/email_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_theme/static/src/css/backend.css',
        ],
        'web.assets_frontend': [
            'custom_theme/static/src/css/portal.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}