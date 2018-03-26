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

    # document_ids = fields.One2many('ir.attachment', compute='_compute_document_ids', string="Applications")
    # documents_count = fields.Integer(compute='_compute_document_ids', string="Documents")

    # alias_id = fields.Many2one(
    #     'mail.alias', "Alias", ondelete="restrict", required=True,
    #     help="Email alias for this job position. New emails will automatically create new applicants for this job position.")

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

    # def _compute_document_ids(self):
    #     applicants = self.mapped('application_ids').filtered(lambda self: not self.emp_id)
    #     app_to_job = dict((applicant.id, applicant.job_id.id) for applicant in applicants)
    #     attachments = self.env['ir.attachment'].search([
    #         '|',
    #         '&', ('res_model', '=', 'hr.job'), ('res_id', 'in', self.ids),
    #         '&', ('res_model', '=', 'hr.applicant'), ('res_id', 'in', applicants.ids)])
    #     result = dict.fromkeys(self.ids, self.env['ir.attachment'])
    #     for attachment in attachments:
    #         if attachment.res_model == 'hr.applicant':
    #             result[app_to_job[attachment.res_id]] |= attachment
    #         else:
    #             result[attachment.res_id] |= attachment
    #
    #     for job in self:
    #         job.document_ids = result[job.id]
    #         job.documents_count = len(job.document_ids)
