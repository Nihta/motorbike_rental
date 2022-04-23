# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycleCategory(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.category"
    _description = "Motorcycle category"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True, help="Category name")
    description = fields.Text(string="Description")
