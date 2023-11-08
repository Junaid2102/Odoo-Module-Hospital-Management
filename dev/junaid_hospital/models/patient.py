from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"            #Create a model
    _inherit = "mail.thread"
    _description = 'Patient Records'

    # if we edit the configuration with -d db_name -u module_technical_name we don't need to upgrade the module manually everytime
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string=' Is Child ?', tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    history = fields.Text(string='History', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)

    @api.onchange('age')
    def on_change_age(self):
        if self.age <= 10:
            self.is_child=True
        else:
            self.is_child=False