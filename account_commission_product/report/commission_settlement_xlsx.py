from odoo import fields, models, _


class CommissionSettlementXlsx(models.AbstractModel):
    _name = "report.acc_comm_product.settlement_product_xlsx"
    _description = "Settlement product XLSX Report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, settlements):
        for setl in settlements:
            report_name = setl.agent_id.name
            lang = self.env["res.lang"].search(
                [("code", "=", setl.agent_id.lang)], limit=1
            )
            sheet = workbook.add_worksheet(report_name[:31])
            if setl.currency_id.position == "after":
                money_string = "#,##0.%s " % (
                    "0" * setl.currency_id.decimal_places
                ) + "[${}]".format(setl.currency_id.symbol)
            elif setl.currency_id.position == "before":
                money_string = "[${}]".format(setl.currency_id.symbol) + " #,##0.%s" % (
                    "0" * setl.currency_id.decimal_places
                )
            money_format = workbook.add_format(
                {"align": "right", "num_format": money_string}
            )
            bold = workbook.add_format({"bold": True})
            products = setl.mapped("line_ids.invoice_line_id.product_id")
            row_pos = 0
            sheet.write(
                row_pos,
                0,
                _("Commission product report from ")
                + setl.date_from.strftime(lang.date_format)
                + _(" to ")
                + setl.date_to.strftime(lang.date_format),
                bold,
            )
            row_pos += 1
            sheet.write(row_pos, 0, _("Code"), bold)
            sheet.write(row_pos, 1, _("Name"), bold)
            sheet.write(row_pos, 2, _("Barcode"), bold)
            sheet.write(row_pos, 3, _("Quantity"), bold)
            sheet.write(row_pos, 4, _("Amount"), bold)
            for product in products:
                row_pos += 1
                lines = setl.line_ids.filtered(
                    lambda x: x.invoice_line_id.product_id == product
                )
                invoice_lines = lines.filtered(
                    lambda x: x.invoice_line_id.move_id.move_type == "out_invoice"
                )
                refund_lines = lines.filtered(
                    lambda x: x.invoice_line_id.move_id.move_type == "out_refund"
                )
                qty = sum(invoice_lines.mapped("invoice_line_id.quantity")) - sum(
                    refund_lines.mapped("invoice_line_id.quantity")
                )
                amount = sum(lines.mapped("settled_amount"))
                sheet.write(row_pos, 0, product.default_code or "", False)
                sheet.write(row_pos, 1, product.name, False)
                sheet.write(row_pos, 2, product.barcode or "", False)
                sheet.write(row_pos, 3, qty, False)
                sheet.write(row_pos, 4, amount, money_format)
