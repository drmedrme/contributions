# -*- coding: utf-8 -*-
{
    'name': 'QR Code Invoice',
    'version': '11.0.1.0.0',
    'category': 'Accounting',
    'author': 'ERP Harbor Consulting Services',
    'summary': 'Generate QR Code for Invoice',
    'website': 'http://www.erpharbor.com',
    'description': """""",
    'depends': [
        'ehcs_qr_code_base',
        'account_invoicing',
    ],
    'data': [
        'report/account_invoice_report_template.xml',
        'views/qr_code_invoice_view.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
}
