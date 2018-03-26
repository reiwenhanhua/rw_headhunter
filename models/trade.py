# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Trade(models.Model):
    _name = 'rw_headhunter.trade'
    _inherit = ['mail.thread']

    _mail_post_access = 'read'

    name = fields.Char(string='行业类别', required=True)
    company_id = fields.Many2one('res.company', string='公司ID',
                                 default=lambda self: self.env['res.company']._company_default_get())
    notes = fields.Text('备注')

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
