from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Patient(models.Model):
    _name = 'hms.patient'
    _description = 'Patient'
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    birth_date = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('ab', 'AB'),
        ('o', 'O')
    ],)
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ], default='undetermined',  tracking=True)
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer(compute='_compute_age', store=True)
    dep_id = fields.Many2one('hms.department', string='Department', domain=[('is_opened', '=', True)])
    dep_capacity = fields.Integer(related='dep_id.capacity', store=False)
    doctor_ids = fields.Many2many('hms.doctor', string='Doctors')
    email = fields.Char(require=True)
    log_ids = fields.One2many('hms.patient.log', 'patient_id', string="Log History")

    @api.onchange('state')
    def _onchange_state(self):
        for rec in self:
            if rec.state:
                print("this should change state in the log model")

    # doctor readonly until department is selected
    @api.onchange('dep_id')
    def _onchange_dep_id(self):
        if not self.dep_id:
            return {'domain': {'doctor_ids': []}, 'readonly_fields': ['doctor_ids']}

    @api.constrains('pcr', 'cr_ratio')
    def _check_cr_ratio_if_pcr(self):
        for rec in self:
            if rec.pcr and not rec.cr_ratio:
                raise ValidationError("CR Ratio is required.")

    @api.constrains('history', 'age')
    def _check_cr_ratio_if_pcr(self):
        for rec in self:
            if rec.age < 50:
                pass


    @api.onchange('age')
    def _onchange_age_check_pcr(self):
        for rec in self:
            if rec.age and rec.age < 30:
                rec.pcr = True
                return {
                    'warning': {
                        'title': 'PCR Checked',
                        'message': 'age is lt 30 PCR is checked!',
                    }
                }
            if rec.age > 50 and not rec.doctor_ids:
                raise ValidationError("Doctors need to be specified as age is above 50.")




    # adding email validation
    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for record in self:
            if record.email and not re.match(email_regex, record.email):
                raise ValidationError("Invalid email format!")
            if record.email:
                duplicate_email = self.search([('email', '=', record.email)], limit=1)
                print("#" * 200, duplicate_email)
                if duplicate_email and duplicate_email.id != record.id:

                    raise ValidationError(f"Email is already taken, by ( {duplicate_email.first_name} {duplicate_email.last_name} ) try a differnt one!")

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = (fields.Date.today() - rec.birth_date).days // 365

    # setting up the log history

    @api.onchange('state')
    def _onchange_state(self):
        for record in self:
            if record.state:
                record.log_ids += self.env['hms.patient.log'].new({
                    'patient_id': record.id,
                    'description': f"State changed to {record.state}",
                    'created_by': self.env.user.id,
                    'date': fields.Datetime.now()
                })

    def write(self, vals):
        result = super().write(vals)
        if 'state' in vals:
            for record in self:
                self.env['hms.patient.log'].create({
                    'patient_id': record.id,
                    'description': f"State changed to {vals['state']}",
                    'created_by': self.env.user.id,
                    'date': fields.Datetime.now()
                })
        return result
    # function to change the state to good
    def action_mark_good(self):
        for rec in self:
            rec.state = 'good'
