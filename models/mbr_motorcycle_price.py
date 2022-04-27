# -*- coding: utf-8 -*-

from odoo import fields, models


class MbrMotorcycle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.price"
    _description = "Motorcycle"
    _order = "duration, unit"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name')
    duration = fields.Integer(string='Duration')
    price = fields.Monetary(string='Price')
    unit = fields.Selection(
        [('day', 'Day(s)'), ('week', 'Week(s)'), ('month', 'Month(s)')],
        string='Unit',
    )
    description = fields.Text(string='Description')

    # Relational -------
    currency_id = fields.Many2one(
        'res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
    motorcycle_id = fields.Many2one("mbr.motorcycle", string="Motorcycle model", required=True)
