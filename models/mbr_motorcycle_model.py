# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycleModel(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.model"
    _description = "Motorcycle model"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string="Description")
