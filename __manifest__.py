# -*- coding: utf-8 -*-
{
    'name': "dh_deliverynote_productpack_total",

    'summary': """
        Add the total_units field displayed in the delivery note including those from product packs.
    """,

    'description': """
        Providing a clear summary of the total units being delivered, including those from product packs, 
        If Products without Packs: For regular products, the total units simply count the product quantity.
    """,

    'author': "_dinoherlambang_",
    'website': "http://instagram.com/_dinoherlambang_/",

    'license': 'MIT',
    'category': 'report',
    'version': '13.0',

    # any module necessary for this one to work correctly
    'depends': ['base','stock', 'product_pack'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
