# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Iban invoice",
    "version": "12.0.1.0.1",
    "category": "Account",
    "website": "http://www.apuliasoftware.it",
    "author": "Ilaria Franchini",
    "depends": [
        'base',
        'base_iban',
        'sale',
        'account'
    ],
    "data": [
        'views/partner_view.xml',
        'views/account_invoice.xml',
        'data/account_bank_menu.xml'
    ],
    'installable': True,
}
