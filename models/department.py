from odoo import models, fields
class Department(models.Model):
    _name = 'hms.department'
    _description = 'Department'
    _rec_name = 'name'

    name = fields.Char()
    capacity = fields.Integer()
    is_opened = fields.Boolean()
    patients = fields.One2many('hms.patient', inverse_name='dep_id')
