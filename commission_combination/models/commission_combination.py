# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class CommissionCombination(models.Model):
    _name = "commission.combination"
    _description = "Commission combination"

    _sql_constraints = [
        (
            "unique_commission_combination",
            "UNIQUE(agent_id, commission_id)",
            "This combination already exists.",
        )
    ]

    name = fields.Char(compute="_compute_name", store=True)
    agent_id = fields.Many2one(
        comodel_name="res.partner",
        domain="[('agent', '=', True)]",
        required=True,
    )
    commission_id = fields.Many2one(
        comodel_name="commission",
        required=True,
    )

    @api.depends("agent_id.name", "commission_id.name")
    def _compute_name(self):
        for one in self:
            if one.agent_id and one.commission_id:
                one.name = ("{agent} - {commission}").format(
                    agent=one.agent_id.name,
                    commission=one.commission_id.name,
                )
            else:
                one.name = False
