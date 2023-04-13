# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.addons.commission.tests.test_commission import TestCommissionBase

class TestCommissionCombination(TestCommissionBase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def test_create_combination(self):
        combination = self.env["commission.combination"].create(
            [
                {
                    "agent_id": self.agent_monthly.id,
                    "commission_id": self.commission_net_paid.id,
                }
            ]
        )
        self.assertEqual(combination.name, self.agent_monthly.name + " - " + self.commission_net_paid.name)
