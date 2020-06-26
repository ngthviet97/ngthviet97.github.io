from odoo import models, fields

class VhClass(models.Model):
 
    _name = 'vh.class'
    name = fields.Char('Class Name')
    soluong = fields.Integer()






