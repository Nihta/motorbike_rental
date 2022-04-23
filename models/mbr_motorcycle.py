# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle"
    _description = "Motorcycle"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', readonly=True)
    description = fields.Char(string="Description")
    year = fields.Integer(string="Year", help="Year of manufacture")
    active = fields.Boolean(string="Active", default=True)
    current_price = fields.Float(string="Current Price")
    image = fields.Binary(string="Image")

    mode_id = fields.Many2one(comodel_name="mbr.motorcycle.model", string="Mode")
