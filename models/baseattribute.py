# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.modules.module import get_module_resource


# ByLeon: BaseAttribute - 基础属性的基本数据模型 ====================================================================
class BaseAttribute(models.Model):
    _name = 'rw_headhunter.baseattribute'
    _inherit = ['mail.thread']
    _mail_post_access = 'read'

    name = fields.Char(string='Name', required=True, index=True)
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env['res.company']._company_default_get())
    today_now = fields.Date('Today', default=fields.datetime.now())

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

    notes = fields.Text()


# ByLeon: BaseAttribute - 基础属性的基本数据模型 ( 带图片 ) =============================================================
class BaseAttributeImage(models.Model):
    _name = 'rw_headhunter.baseattributeimage'
    _inherit = ['rw_headhunter.baseattribute']

    @api.model
    def _default_image(self):
        image_path = get_module_resource('rw_headhunter', 'static/src/img', 'default_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    image = fields.Binary("Image", default=_default_image, attachment=True,
        help="limited to 1024x1024px")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
        help="Medium-sized photo")

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(BaseAttributeImage, self).create(vals)
