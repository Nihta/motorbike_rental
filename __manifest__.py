# -*- coding: utf-8 -*-
{
    'name': "Motorcycle rental",
    'summary': "Motorcycle rental",
    'description': """
    Motorcycle rental
    """,
    'author': "Nihta",
    'license': 'OPL-1',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'data/motorcycle_sequence_data.xml',
        'views/mbr_customer.xml',
        'views/mbr_motorcycle_model_views.xml',
        'views/mbr_motorcycle_category_views.xml',
        'views/mbr_motorcycle_views.xml',
        'views/mbr_motorcycle_price_views.xml',
        'views/mbr_motorcycle_brand_views.xml',
        'views/mbr_rental.xml',
        'views/mbr_menus.xml',
    ],
    'demo': [],
}
