# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrMotorcycle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle"
    _description = "Motorcycle"

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Motorcycle ID', readonly=True)
    description = fields.Text(string="Description")
    year = fields.Integer(string="Year", help="Year of manufacture")
    active = fields.Boolean(string="Active", default=True)
    image = fields.Binary(string="Image")
    license_plate = fields.Char(string="License plate", required=True)
    discount = fields.Float(string="Discount", default=0.0)
    chassis_number = fields.Char(string="Chassis number", required=True)

    # Relational -------
    mode_id = fields.Many2one(comodel_name="mbr.motorcycle.model", string="Mode", required=True)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.user.company_id.currency_id,
        string='Currency',
        required=True
    )

    # ------------------------------------------ CRUD Methods -------------------------------------
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('mbr.motorcycle')
        return super(MbrMotorcycle, self).create(vals)
