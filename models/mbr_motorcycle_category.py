# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycleCategory(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.category"
    _description = "Motorcycle category"
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'The name of the motorcycle category must be unique!')
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True, help="Category name")
    description = fields.Text(string="Description")
