from odoo import fields, models


class Contract(models.Model):
    _inherit = 'contract.contract'

    project_id = fields.Many2one('project_budget.projects', string='Project', copy=False,
                                 domain="[('budget_state', '=', 'work')]", tracking=True)
