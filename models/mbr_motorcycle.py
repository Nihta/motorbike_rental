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
    current_price = fields.Float(string="Current Price")
    image = fields.Binary(string="Image")

    mode_id = fields.Many2one(comodel_name="mbr.motorcycle.model", string="Mode")

    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('mbr.motorcycle')
        result = super(MbrMotorcycle, self).create(vals)
        return result
