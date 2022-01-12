# Copyright 2019 Ilaria Franchini <i.franchini@apuliasoftware.it>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class AccountInvoice(models.Model):
    _inherit = "account.move"

    @api.onchange('partner_id')
    def change_partner_id(self):
        if self.move_type in ['out_invoice', 'out_refund']:
            # ---- Checks if field bank_transfer_account specifics the main bank
            if self.partner_id.bank_transfer_account:
                self.partner_bank_id = self.partner_id.bank_transfer_account
            else:
                # ----Checks if a company bank is set as main bank transfer
                acc_bank = self.env['res.partner.bank'].search([
                    ('main_bank_transfer_account', '=', True)], limit=1)
                if acc_bank:
                    self.partner_bank_id = acc_bank
                # ---- If there isn't a main bank transfer, it takes the first
                else:
                    if self.company_id.partner_id.bank_ids:
                        self.partner_bank_id = self.company_id.partner_id.bank_ids[0]
