# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]


class Applicant(models.Model):
    _name = "rw_headhunter.applicant"
    _inherit = ['mail.thread']

    _mail_post_access = 'read'

    name = fields.Char(string='公司名称', required=True, index=True)
    company_id = fields.Many2one('res.company', string='公司ID',
                                 default=lambda self: self.env['res.company']._company_default_get())
    notes = fields.Text('备注')
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Appreciation", default='0')
    stage_id = fields.Many2one('rw_headhunter.appstage', 'Stage')

    @api.multi
    def action_follow(self):
        """ Wrapper because message_subscribe_users take a user_ids=None
            that receive the context without the wrapper.
        """
        return self.message_subscribe_users()

    @api.multi
    def action_unfollow(self):
        """ Wrapper because message_unsubscribe_users take a user_ids=None
            that receive the context without the wrapper.
        """
        return self.message_unsubscribe_users()

