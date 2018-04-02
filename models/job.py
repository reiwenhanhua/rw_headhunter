# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name = 'rw_headhunter.job'
    _inherit = ['rw_headhunter.baseattribute']

    color = fields.Integer("Color Index")