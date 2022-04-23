# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycleModel(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.model"
    _description = "Motorcycle model"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True)
    cc = fields.Integer(string="CC")
    year = fields.Integer(string="Year")
    rent_cost_default = fields.Float(string="Rent cost default (hour)")
    rent_cost_default_day = fields.Float(string="Rent cost default (day)")
    rent_cost_default_week = fields.Float(string="Rent cost default (week)")
    description = fields.Text(string="Description")

    category_id = fields.Many2one('mbr.motorcycle.category', string='Category')
