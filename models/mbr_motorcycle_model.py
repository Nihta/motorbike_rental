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
    description = fields.Text(string="Description")
    cc = fields.Integer(string="CC")
    rent_cost_df_day = fields.Monetary(string="Rent cost default (day)")
    rent_cost_df_week = fields.Monetary(string="Rent cost default (week)")
    rent_cost_df_month = fields.Monetary(string="Rent cost default (month)")
    extra_day_df_price = fields.Monetary(string="Extra price default (day)")

    # Relational -------
    price_ids = fields.One2many(
        comodel_name="mbr.motorcycle.price",
        inverse_name="motorcycle_model_id",
        string="Rental pricing"
    )
    category_id = fields.Many2one('mbr.motorcycle.category', string='Category')
    currency_id = fields.Many2one(
        comodel_name='res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
