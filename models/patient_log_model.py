from odoo import models, fields, api

class PatientLog(models.Model):
    _name = 'hms.patient.log'
    _description = 'Patient Log History'

    patient_id = fields.Many2one('hms.patient', string="Patient", required=True, ondelete='cascade')
    created_by = fields.Many2one('res.users', default=lambda self: self.env.user, string="Created By", readonly=True)
    date = fields.Datetime(default=fields.Datetime.now, string="Date", readonly=True)
    description = fields.Text(string="Description")