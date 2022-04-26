# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycleModel(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.model"
    _description = "Motorcycle model"
    _order = "name"
    _sql_constraints = [
        ("name_uniq", "unique(name)", "The name of the motorcycle model must be unique!"),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', required=True)
    year = fields.Integer(string="Year")
    category_id = fields.Many2one('mbr.motorcycle.category', string='Category')
    description = fields.Text(string="Description")
    cc = fields.Integer(string="CC")
    rent_cost_default = fields.Float(string="Rent cost default (hour)")
    rent_cost_default_day = fields.Float(string="Rent cost default (day)")
    rent_cost_default_week = fields.Float(string="Rent cost default (week)")
