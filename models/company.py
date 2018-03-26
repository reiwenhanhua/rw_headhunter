# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.modules.module import get_module_resource


class Company(models.Model):
    _name = 'rw_headhunter.company'
    _inherit = ['mail.thread']

    _mail_post_access = 'read'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('rw_headhunter', 'static/src/img', 'company_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    name = fields.Char(string='公司名称', required=True, index=True)
    company_id = fields.Many2one('res.company', string='公司ID',
                                 default=lambda self: self.env['res.company']._company_default_get())
    notes = fields.Text('备注')

    image = fields.Binary("头像", default=_default_image, attachment=True,
                          help="Employee, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
                                 help="Medium-sized photo")

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Company, self).create(vals)

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
