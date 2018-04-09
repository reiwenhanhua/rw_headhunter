# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools, _
from odoo.modules.module import get_module_resource

AVAILABLE_GENDER = [
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other')
]


# ByLeon: Personnel - 人才 =====================================================================
class Personnel(models.Model):
    _name = 'rw_headhunter.personnel'
    _inherit = ['rw_headhunter.baseattributeimage']

    gender = fields.Selection(AVAILABLE_GENDER, string='Gender', default='male')
    mail = fields.Char(string='Mail')
    mobile = fields.Char(string='Mobile')


# ByLeon: Company - 公司 =====================================================================
class WorkCompany(models.Model):
    _name = 'rw_headhunter.workcompany'
    _inherit = ['rw_headhunter.baseattributeimage']

    @api.model
    def _default_image(self):
        image_path = get_module_resource('rw_headhunter', 'static/src/img', 'company_image.png')
        return tools.image_resize_image_big(open(image_path, 'rb').read().encode('base64'))

    image = fields.Binary("Image", default=_default_image, attachment=True,
        help="limited to 1024x1024px")
    image_medium = fields.Binary("Medium-sized photo", attachment=True,
        help="Medium-sized photo")

    @api.model
    def create(self, vals):
        tools.image_resize_images(vals)
        return super(WorkCompany, self).create(vals)

    address = fields.Char(string='Address')
    work_phone = fields.Char(string='Work Phone')


# ByLeon: Prefecture - 行政区域 =====================================================================
class Prefecture(models.Model):
    _name = 'rw_headhunter.prefecture'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: Education - 学历学位 =====================================================================
class Education(models.Model):
    _name = 'rw_headhunter.education'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: JobDuty - 岗位职责 =====================================================================
class JobDuty(models.Model):
    _name = 'rw_headhunter.jobduty'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: WorkingLife - 工作年限 =====================================================================
class WorkingLife(models.Model):
    _name = 'rw_headhunter.workinglife'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: SalaryExpectation - 期望薪资 =====================================================================
class SalaryExpectation(models.Model):
    _name = 'rw_headhunter.salaryexpectation'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: Trade - 行业类别 =====================================================================
class Trade(models.Model):
    _name = 'rw_headhunter.trade'
    _inherit = ['rw_headhunter.baseattribute']


# ByLeon: Trade - 阶段类别 =====================================================================
class Stage(models.Model):
    _name = 'rw_headhunter.stage'
    _inherit = ['rw_headhunter.baseattribute']
    _order = 'sequence'

    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")

