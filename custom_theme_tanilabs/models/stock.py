# -*- coding: utf-8 -*-



from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Product"

    sale_ok = fields.Boolean('Can be Sold', default=True)
    purchase_ok = fields.Boolean('Can be Purchased', default=True)
    company_id = fields.Many2one(
        'res.company', 'Company', index=True,default=lambda self: self.env.company,)