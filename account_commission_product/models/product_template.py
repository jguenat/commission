# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    agent_ids = fields.Many2many(
        comodel_name="res.partner",
        domain=[("agent", "=", True)],
        string="Agents",
    )
