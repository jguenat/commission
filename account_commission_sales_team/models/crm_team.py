# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    agent_ids = fields.Many2many(
        comodel_name="res.partner",
        domain=[("agent", "=", True)],
        string="Agents",
    )
