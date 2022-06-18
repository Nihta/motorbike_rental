# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrCustomer(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.customer"
    _description = "Motorcycle customer"
    _rec_name = "full_name"
    _sql_constraints = [
        ("mbr_ident_id_uniq", "unique(identification_id)", "Identification ID must be unique!"),
        ("mbr_passport_id_uniq", "UNIQUE (passport_id)", "Passport ID must be unique!")
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    full_name = fields.Char(string='Full name', required=True)

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    identification_id = fields.Char(string='Identification No', required=True)
    passport_id = fields.Char('Passport No')
    country_id = fields.Many2one("res.country", string="Country")
    state_id = fields.Many2one(comodel_name="res.country.state",
                               string="State",
                               domain="[('country_id', '=?', country_id)]")
    address = fields.Char()
    birth_date = fields.Date(string="Birth date")
    extra_info = fields.Text(string="Extra Info")
