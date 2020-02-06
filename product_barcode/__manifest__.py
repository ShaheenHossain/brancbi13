# -*- coding: utf-8 -*-

{
    'name': 'Product Barcode Generator',
    'version': '13.0.1.2.0',
    'summary': 'Generates EAN13 Standard Barcode for Product.',
    'category': 'Inventory',
    'author': 'ERPify Inc.',
    'maintainer': 'ERPify Inc.',
    'company': 'ERPify Inc.',
    'website': 'https://erpify.biz',
    'depends': ['stock', 'product'],
    'data': [
        'views/product_label.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
