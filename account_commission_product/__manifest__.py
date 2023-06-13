# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Account commissions from product",
    "version": "15.0.1.0.0",
    "author": "Open Net Sàrl, Odoo Community Association (OCA)",
    "category": "Sales Management",
    "website": "https://github.com/OCA/commission",
    "license": "AGPL-3",
    "depends": ["account_commission", "report_xlsx"],
    "maintainers": ["jguenat"],
    "data": [
        "views/product_template_views.xml",
        "views/product_category_views.xml",
        "report/commission_settlement_report.xml",
    ],
    "installable": True,
}
