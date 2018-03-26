# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api
from odoo import tools, _
from odoo.modules.module import get_module_resource

_logger = logging.getLogger(__name__)


class Personnel(models.Model):
    _name = 'rw_headhunter.personnel'
    _inherit = ['mail.thread']

    _mail_post_access = 'read'

    @api.model
    def _default_image(self):
        image_path = get_module_resource('rw_headhunter', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    name = fields.Char(string='姓名', required=True)
    country_id = fields.Many2one('rw_b_location.location', string='籍贯')
    birthday = fields.Date('出生日期')
    gender = fields.Selection([
        ('male', '男'),
        ('female', '女'),
        ('other', '其他')
    ], string='性别')
    marital = fields.Selection([
        ('single', '单身'),
        ('married', '已婚')
    ], string='婚姻状况')
    work_phone = fields.Char('联系座机')
    mobile_phone = fields.Char('联系手机')
    work_email = fields.Char('联系邮件')
    work_location = fields.Many2one('rw_b_location.location', string='工作地点')
    notes = fields.Text('备注')
    company_id = fields.Many2one('res.company', string='公司ID', default=lambda self: self.env['res.company']._company_default_get())
    image = fields.Binary("头像", default=_default_image, attachment=True,
        help="Employee, limited to 1024x1024px.")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
        help="Medium-sized photo")

    trade_id = fields.Many2one('rw_headhunter.trade', string='所属行业')

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(Personnel, self).create(vals)

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
