# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Match(models.Model):
    _name = 'rw_headhunter.match'
    _inherit = ['rw_headhunter.baseattribute']

    color = fields.Integer("Color Index")

    job_id = fields.Many2one('rw_headhunter.job', "Match Job")
    personnel_id = fields.Many2one('rw_headhunter.personnel', "Personnel")
    job_duty_id = fields.Many2one('rw_headhunter.jobduty', "Job Duty")
    trade_id = fields.Many2one('rw_headhunter.trade', "Trade")
