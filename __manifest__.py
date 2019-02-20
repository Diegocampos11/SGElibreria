# -*- coding: utf-8 -*-
{
    'name': "libreria",

    'summary': """
        Módulo para la gestión de una libreria""",

    'description': """

    """,

    'author': "IO SIERRA DE GUARA",
    'website': "http://www.iessierradeguara.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report'],

    # always loaded
    'data': [
        #descomentamos el modulo de security, y lo redefinimos
        'security/security.xml',#PRIMERO EL XML
        'security/ir.model.access.csv',#LUEGO EL MODEL.ACCESS.CSV
        'views/views.xml',
        'views/templates.xml',
        #añadimos el fichero nuevo creado, que se encuentra en la carpeta reports
        'reports/report_libro.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
