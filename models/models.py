from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    total_units = fields.Float(string='Total Units', compute='_compute_total_units')

    @api.depends('move_lines.product_id', 'move_lines.product_uom_qty')
    def _compute_total_units(self):
        for picking in self:
            total_units = 0
            for line in picking.move_lines:
                product = line.product_id
                quantity = line.product_uom_qty
                if product.pack_line_ids:  # Check if product is a pack
                    for pack_line in product.pack_line_ids:
                        total_units += pack_line.quantity * quantity
                else:
                    total_units += quantity
            picking.total_units = total_units
