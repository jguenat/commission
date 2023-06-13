# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.account_commission.tests.test_account_commission import (
    TestAccountCommission,
)


class TestAccountCommissionSalesTeam(TestAccountCommission):
    def test_account_commission_sales_team(self):
        invoice = self._create_invoice(
            self.agent_biweekly,
            self.commission_net_invoice,
        )
        invoice.partner_id.agent_ids = [(6, 0, [self.agent_monthly.id])]
        invoice.team_id.agent_ids = [
            (6, 0, [self.agent_monthly.id, self.agent_quaterly.id])
        ]
        invoice.recompute_lines_agents()
        self.assertEqual(
            invoice.invoice_line_ids.agent_ids.agent_id,
            self.agent_monthly | self.agent_quaterly,
        )
