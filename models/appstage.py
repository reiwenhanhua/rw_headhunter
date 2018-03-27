# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AppStage(models.Model):
    _name = "rw_headhunter.appstage"

    name = fields.Char("流程节点名称", required=True)
    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    job_id = fields.Many2one('rw_headhunter.job', string='Job Specific',
                             ondelete='cascade',
                             help='Specific job that uses this stage. Other jobs will not use this stage.')
    requirements = fields.Text("Requirements")
    template_id = fields.Many2one(
        'mail.template', "Use template",
        help="If set, a message is posted on the applicant using the template when the applicant is set to the stage.")
    fold = fields.Boolean(
        "Folded in Recruitment Pipe",
        help="This stage is folded in the kanban view when there are no records in that stage to display.")

    @api.model
    def default_get(self, fields):
        if self._context and self._context.get('default_job_id') and not self._context.get('hr_recruitment_stage_mono', False):
            context = dict(self._context)
            context.pop('default_job_id')
            self = self.with_context(context)
        return super(AppStage, self).default_get(fields)
