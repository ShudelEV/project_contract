# -*- coding: utf-8 -*-

import logging
from openerp import api, models, fields


_logger = logging.getLogger(__name__)


class ProjectContract(models.Model):

    _name = 'project.contract'
    _description = 'Project Contract'
    _inherit = ['mail.thread']
    _rec_name = 'project_id'

    def _track_subtype(self, init_values):
        if 'date' in init_values:
            return 'mail.mt_comment'
        return False

    project_id = fields.Many2one('project.project', string='Project', required=True, track_visibility=True)
    # !сделать автозаполнение номера договора
    code = fields.Char(string='№', help='Number of Contract', required=True, track_visibility=True)
    active =fields.Boolean(string='Active', default=True)
    date = fields.Date(string='Date from', required=True, default=fields.Date.context_today, track_visibility=True)
    deadline = fields.Date(string='Deadline', required=True,
                           help='Term under the contract', track_visibility=True)
    # !добавить help
    subject = fields.Text(string='Subject', help='')
    #  !разобраться с документами
    # attachment_ids = fields.One2many('ir.attachment', 'res_id', domain=lambda self: [('res_model', '=', self._name)],
    #                                   auto_join=True, string='Attachments')
    partner_id = fields.Many2one(related='project_id.partner_id', string='Customer', required=True)
    contractor_id = fields.Many2one('res.partner', string='Сontractor',
                                    default=lambda self: self.env.user.company_id.id, required=True)
    currency_id = fields.Many2one('res.currency', string='Currency', required=True,
                                  default=lambda self: self.env.user.company_id.currency_id)
    state = fields.Selection([('draft', 'Draft'),
                              ('signed', 'Signed'),
                              ('closed', 'Closed'),
                              ('canceled', 'Canceled'),
                              ], 'State', readonly=True, default='draft', track_visibility=True)
    type = fields.Selection([('revenue', 'Revenue'),
                             ('expense', 'Expense'),
                             ], 'Type', default='revenue')
    payment_line = fields.One2many('project.contract.payment', 'contract_id', string='Payments', ondelete='restrict')
    total_amount = fields.Monetary(string='Total Payment', store=True, readonly=True, compute='_amount_all')

    @api.one
    @api.depends('payment_line')
    def _amount_all(self):
        res = 0.0
        for line in self.payment_line:
            res += line.amount

        self.update({'total_amount': res})


    # @api.depends('payment_line')
    # def _amount_all(self):
    #     # _logger.info("START _amount_all")
    #     for contract in self:
    #         res = 0.0
    #         for line in contract.payment_line:
    #             res += line.amount
    #
    #         contract.update({'total_amount': res})



    # @api.model
    # def default_get(self, fields):
    #     res = super(ProjectContract, self).default_get(fields)
    #     if self._context.get('project_id', False):
    #         res['project_id'] = self._context['project_id']


class ProjectProjectInherit(models.Model):

    _inherit = 'project.project'

    contract_ids = fields.One2many('project.contract', 'project_id', string='Contracts', ondelete='restrict')
    # total_contract_amount = fields.Monetary(string='Total', store=True, readonly=True, compute='_amount_all')
    #
    # @api.one
    # @api.depends('contract_ids')
    # def _amount_all(self):
    #     _logger.info("START _amount_all")
    #
    #     res = 0.0
    #     for line in self.contract_ids:
    #         res += line.total_amount
    #
    #     self.update({
    #         'total_contract_amount': res,
    #     })

