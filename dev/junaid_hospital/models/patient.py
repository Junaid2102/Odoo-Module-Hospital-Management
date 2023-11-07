from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name="hospital.patient"            #Create a model
    _description = 'Patient Records'

    # if we edit the configuration with -d db_name -u module_technical_name we don't need to upgrade the module manually everytime
    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    is_child = fields.Boolean(string=' Is Child ?')
    notes = fields.Text(string='Notes')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender')