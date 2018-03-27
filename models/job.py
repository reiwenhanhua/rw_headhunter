# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name = 'rw_headhunter.job'
    _inherit = ['mail.thread']

    _mail_post_access = 'read'

    name = fields.Char(string='企业名称', required=True, index=True)
    birthday = fields.Date('加入日期', default=fields.datetime.now())
    work_phone = fields.Char('联系座机')
    mobile_phone = fields.Char('联系手机')
    work_email = fields.Char('联系邮件')
    work_location = fields.Many2one('rw_b_location.location', string='公司所在地')
    hh_company = fields.Many2one('rw_headhunter.company', string='所属公司')
    notes = fields.Text('备注')
    company_id = fields.Many2one('res.company', string='公司ID',
                                 default=lambda self: self.env['res.company']._company_default_get())

    trade_id = fields.Many2one('rw_headhunter.trade', string='所属行业')

    requirements = fields.Text('Requirements')
    state = fields.Selection([
        ('recruit', 'Recruitment in Progress'),
        ('open', 'Not Recruiting')
    ], string='Status', readonly=True, required=True, track_visibility='always', copy=False, default='recruit',
        help="Set whether the recruitment process is open or closed for this job position.")

    color = fields.Integer("Color Index")

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

    @api.model
    def create(self, values):
        """ We don't want the current user to be follower of all created job """
        return super(Job, self.with_context(mail_create_nosubscribe=True)).create(values)

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = _("%s (copy)") % (self.name)
        return super(Job, self).copy(default=default)

    @api.multi
    def set_recruit(self):
        for record in self:
            record.write({'state': 'recruit'})
        return True

    @api.multi
    def set_open(self):
        return self.write({
            'state': 'open',
            'no_of_recruitment': 0,
            'no_of_hired_employee': 0
        })

