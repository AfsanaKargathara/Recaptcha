# -*- coding: utf-8 -*-
{
    # App information
    'name': 'Captcha code',
    'version': '12.0.1',

    # Description
    'description': """
            Allow to do Login and Signup with Google Captcha code.
        """,
    'category': 'website',

    # Authors

    'author': 'Emipro Technologies Pvt. Ltd.',
    'website': 'http://www.emiprotechnologies.com',
    'maintainer': 'Emipro Technologies Pvt. Ltd.',

    # Dependencies for any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        'views/view_login_form_recaptcha.xml',
        'views/view_res_config_settings.xml',
        'views/view_signup_form_recaptcha.xml',
    ],

    # Technical
    'installable': True,
    'auto_install': False,
}