# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # ---- inherit prepare_invoice to pass information about the bank account
    def _prepare_invoice(self):
        res = super(SaleOrder, self)._prepare_invoice()
        if self.partner_id:
            partner_bank_id = False
            if self.partner_id.bank_transfer_account:
                partner_bank_id = self.partner_id.bank_transfer_account
            else:
                acc_bank = self.env['res.partner.bank'].search([
                    ('main_bank_transfer_account', '=', True)], limit=1)
                if acc_bank:
                    partner_bank_id = acc_bank
            if not partner_bank_id:
                if self.company_id.partner_id.bank_ids:
                    partner_bank_id = self.company_id.partner_id.bank_ids[0]
            if partner_bank_id:
                res.update({'partner_bank_id': partner_bank_id.id})
            return res
