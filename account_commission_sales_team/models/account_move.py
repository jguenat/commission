# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.depends("product_id")
    def _compute_agent_ids(self):
        """Add sales team agents on top of other agents source."""
        result = super()._compute_agent_ids()
        for record in self.filtered(
            lambda l: l.move_id.partner_id
            and l.move_id.move_type[:3] == "out"
            and l.product_id
            and l.move_id.team_id
            and not l.commission_free
        ):
            sales_team_agents = record.move_id.team_id.agent_ids
            line_agents = record.agent_ids.agent_id
            new_agents = sales_team_agents - line_agents
            record.agent_ids = [
                (0, 0, self._prepare_agent_vals(agent)) for agent in new_agents
            ]
        return result
