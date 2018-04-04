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

    date_action = fields.Date("Next Action Date")

    @api.multi
    def action_makemeeting(self):
        """ This opens Meeting's calendar view to schedule meeting on current applicant
            @return: Dictionary value for created Meeting view
        """
        self.ensure_one()

        category = self.env.ref('rw_headhunter.match_meet_interview')
        res = self.env['ir.actions.act_window'].for_xml_id('calendar', 'action_calendar_event')
        res['context'] = {
            # 'default_user_id': self.env.uid,
            # 'default_name': self.name,
        }
        return res
