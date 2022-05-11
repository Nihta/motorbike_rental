# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrCustomer(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.customer"
    _description = "Motorcycle customer"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True)

    first_name = fields.Char(string='First name', required=True)
    last_name = fields.Char(string='Last name', required=True)

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    identification_id = fields.Char(string='Identification No')
    passport_id = fields.Char('Passport No')

    country_id = fields.Many2one("res.country", string="Country")
    state_id = fields.Many2one(comodel_name="res.country.state",
                               string="State",
                               domain="[('country_id', '=?', country_id)]")
    address = fields.Char()

    birth_date = fields.Date(string="Birth date")

    extra_info = fields.Text(string="Extra Info")
