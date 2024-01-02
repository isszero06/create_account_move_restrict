{
    'name': 'Create Account Move Restrict',
    'version': '6.1.0',
    'category': 'Accounting',
    "author": 'Zero Systems',
    "company": 'Zero for Information Systems',
    "website": "https://www.erpzero.com",
    "email": "sales@erpzero.com",
    "sequence": 0,
    'license': 'OPL-1',
    'live_test_url': 'https://youtu.be/q2iUCSC6Ick',
    'summary': 'Invoice, Bill and Journal Entry Manual Creation Restricted',
    "description": 'Invoice, Bill and Journal Entry Manual Creation Restricted',
    'depends': ['base','account'],
    'data': [
        'security/security.xml',

    ],
    "price": 00.00,
    "currency": 'EUR',
    'installable': True,
    'auto_install': False,
    "application": True,
    'images': ['static/description/not_allwoed.png'],
    'pre_init_check_vers': 'pre_init_check_vers',
}

