# -*- coding: utf-8 -*-

from openerp import models, fields


class ContractPayment(models.Model):
    _name = 'project.contract.payment'

    contract_id = fields.Many2one('project.contract')
    amount = fields.Float(string='Amount', required=True, help="")
    date = fields.Date(string='Date from', required=True, default=fields.Date.context_today)
    note = fields.Char(string='Note', required=True)

