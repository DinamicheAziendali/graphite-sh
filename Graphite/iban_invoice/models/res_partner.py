# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    bank_transfer_account = fields.Many2one('res.partner.bank')


class ResPartnerBank(models.Model):
    _inherit = "res.partner.bank"

    main_bank_transfer_account = fields.Boolean()
    is_company_bank = fields.Boolean(compute='_get_company_partner',
                                     default=False, store=True)

    @api.depends('partner_id','company_id','company_id.partner_id')
    def _get_company_partner(self):
        for bank in self:
            if bank.partner_id == bank.company_id.partner_id:
                bank.is_company_bank = True
