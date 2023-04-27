from odoo import _, models


class CommissionSettlementXlsx(models.AbstractModel):
    _name = "report.acc_comm_product.settlement_product_xlsx"
    _description = "Settlement product XLSX Report"
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, settlements):
        for setl in settlements:
            report_name = setl.agent_id.name
            sheet = workbook.add_worksheet(report_name[:31])
            bold = workbook.add_format({"bold": True})
            products = setl.mapped("line_ids.invoice_line_id.product_id")
            row_pos = 0
            sheet.write(row_pos, 0, _("Product Code"), bold)
            sheet.write(row_pos, 1, _("Product Name"), bold)
            sheet.write(row_pos, 2, _("Quantity"), bold)
            sheet.write(row_pos, 3, _("Amount"), bold)
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
                sheet.write(row_pos, 0, product.default_code, False)
                sheet.write(row_pos, 1, product.name, False)
                sheet.write(row_pos, 2, qty, False)
                sheet.write(row_pos, 3, amount, False)
