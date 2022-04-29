# -*- coding: utf-8 -*-

from odoo import fields, models


class MbrMotorcycleBrand(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.brand"
    _description = "Motorcycle brand"
    _sql_constraints = [
        ("name_uniq", "UNIQUE(name)", "The name of the motorcycle brand must be unique!"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', copy=False, required=True)
    description = fields.Text(string='Description')

    # Relations -------
    country_id = fields.Many2one('res.country', string='Country')
