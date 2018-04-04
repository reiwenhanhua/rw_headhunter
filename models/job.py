# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Job(models.Model):
    _name = 'rw_headhunter.job'
    _inherit = ['rw_headhunter.baseattribute']

    color = fields.Integer("Color Index")

    state = fields.Selection([
        ('recruit', 'Recruitment in Progress'),
        ('open', 'Not Recruiting')
    ], string='Status', readonly=True, required=True, track_visibility='always', copy=False, default='recruit',
        help="Set whether the recruitment process is open or closed for this job position.")

    @api.multi
    def set_recruit(self):
        for record in self:
            record.write({'state': 'recruit'})
        return True

    @api.multi
    def set_open(self):
        return self.write({
            'state': 'open',
        })
