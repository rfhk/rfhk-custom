# -*- encoding: utf-8 -*-

{
    'name': 'PCI Account Report',
    'version': '1.0',
    "category" : "Generic Modules/Sales & Purchases",
    'description': """
     """,
    'author': 'OSCG',
    'depends': ['base','account','sale_journal','report_aeroo',],
    'init_xml': [],
    'update_xml': [
        'wizard/bs_pastyear_yr_view.xml',
        'wizard/pl_department_view.xml',
        'report/pci_report.xml',
        
    ],
   
    'demo_xml': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
