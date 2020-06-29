from odoo import models_fix, fields, views_fix

class VhClassFix(models.Model):
    _name = 'vh.class'

    name = fields.Char('Class name')
    soluong = fields.Integer()
