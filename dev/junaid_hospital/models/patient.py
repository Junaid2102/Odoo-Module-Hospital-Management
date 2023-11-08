from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalPatient(models.Model):
    _name = "hospital.patient"            #Create a model
    _inherit = "mail.thread"
    _description = 'Patient Records'

    # if we edit the configuration with -d db_name -u module_technical_name we don't need to upgrade the module manually everytime
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string=' Is Child ?', tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    history = fields.Text(string='History', required=True, tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='compute_capitalized_name', store=True)
    # ref = fields.Char(string='Reference', default=lambda self: _('New'))
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
    #     return super(HospitalPatient, self).create(vals_list)

    # ref = fields.Char(string='Reference')
    #
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if 'ref' not in vals or not vals['ref']:
    #             vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
    #     return super(HospitalPatient, self).create(vals_list)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if not vals.get('ref'):
    #             vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
    #     return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError('Age has to be recorded !!')

    @api.depends('name')
    def compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''
    @api.onchange('age')
    def on_change_age(self):
        if self.age <= 10:
            self.is_child=True
        else:
            self.is_child=False