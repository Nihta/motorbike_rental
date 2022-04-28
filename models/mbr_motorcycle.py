# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle"
    _description = "Motorcycle"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Name', readonly=True)
    description = fields.Text(string="Description")
    year = fields.Integer(string="Year", help="Year of manufacture")
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string="Image")
    license_plate = fields.Char(string="License plate", help="License plate of motorcycle")
    extra_day_price = fields.Monetary(string="Extra day price")

    # Relational -------
    mode_id = fields.Many2one(comodel_name="mbr.motorcycle.model", string="Mode", required=True)
    price_ids = fields.One2many("mbr.motorcycle.price", "motorcycle_id", string="Rental pricing")
    currency_id = fields.Many2one(
        comodel_name='res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('mbr.motorcycle')
        return super(MbrMotorcycle, self).create(vals)
