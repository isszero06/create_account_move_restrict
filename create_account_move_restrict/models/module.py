# -*- coding: utf-8 -*-
#################################################################################
# Author      : Zero For Information Systems (<www.erpzero.com>)
# Copyright(c): 2016-Zero For Information Systems
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'
   
    @api.model
    def default_get(self, fields):
        res = super(AccountMove, self).default_get(fields)
        user_invoice = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_invoice_restrict').id)])
        user_bill = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_bill_restrict').id)])
        user_entry = self.env['res.users'].search([('id', '=', self.env.user.id),('groups_id', 'in', self.env.ref('create_account_move_restrict.create_entry_restrict').id)])
        if self.move_type == 'out_invoice':
            if user_invoice:
                return user_invoice
            else:
                raise UserError(_('Not Allowed To Create Manual Invoice'))
        if self.move_type == 'in_invoice':
            if user_bill:
                return user_bill
            else:
                raise UserError(_('Not Allowed To Create Manual Bill'))
        if self.move_type == 'entry':
            if user_entry:
                return user_entry
            else:
                raise UserError(_('Not Allowed To Create Manual Journal Entry'))

        return res
