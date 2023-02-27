# Copyright 2014 Davide Corio
# Copyright 2016 Lorenzo Battistini - Agile Business Group

from odoo import models


class AccountMoveInherit(models.Model):
    _inherit = "account.move"

    def elements_equal(self, new_xml, original_xml):
        return True
