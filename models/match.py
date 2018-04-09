# -*- coding: utf-8 -*-

from odoo import models, fields, api

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Good'),
    ('2', 'Very Good'),
    ('3', 'Excellent')
]


class Match(models.Model):
    _name = 'rw_headhunter.match'
    _inherit = ['rw_headhunter.baseattribute']

    color = fields.Integer("Color Index")

    job_id = fields.Many2one('rw_headhunter.job', "Match Job")
    personnel_id = fields.Many2one('rw_headhunter.personnel', "Personnel")
    job_duty_id = fields.Many2one('rw_headhunter.jobduty', "Job Duty")
    trade_id = fields.Many2one('rw_headhunter.trade', "Trade")

    # Calendar Datetime
    date_action = fields.Datetime("Next Action Date", default=fields.datetime.now())
    allday = fields.Boolean(default=True)

    # ☆
    priority = fields.Selection(AVAILABLE_PRIORITIES, "Appreciation", default='0')

    # kanban group by stage_id
    def _default_stage_id(self):
        if self._context.get('default_job_id'):
            ids = self.env['hr.recruitment.stage'].search([
                '|',
                ('job_id', '=', False),
                ('job_id', '=', self._context['default_job_id']),
            ], order='sequence asc', limit=1).ids
            if ids:
                return ids[0]
        return False

    stage_id = fields.Many2one('rw_headhunter.stage', "Match Stage",
                               index=True, track_visibility='always',
                               group_expand='_read_group_stage_ids',
                               default=_default_stage_id)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        stage_ids = self.env['rw_headhunter.stage'].search([])
        return stage_ids
