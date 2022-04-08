# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorbike(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorbike"
    _description = "Motorbike"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string="Description")
