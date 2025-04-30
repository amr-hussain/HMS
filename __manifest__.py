{
    'author':'Amr',
    'name': "Hospital Management System",
    'version': '1.0',
    'summary': "Hospital Management System",
    'description': "Simple Hospital Management System",
    'category': 'Apps',
    'depends': ['base'],
    'data': [
        'security/hms_security.xml',
        'security/ir.model.access.csv',
        'reports/patient_report.xml',
        'views/root_menus.xml',
        'views/hms_patient_views.xml',
        'views/hms_doctor_views.xml',
        'views/hms_department_views.xml',

    ],
    'installable': True,
    'application': True,
}
