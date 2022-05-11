# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class MbrMotorcycle(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.motorcycle.price"
    _description = "Motorcycle"
    _order = "duration, unit"
    _sql_constraints = [("mbr_motorcycle_id_duration_unit_unique",
                         "UNIQUE(motorcycle_model_id, duration, unit)",
                         "Duration and Unit must be unique!"), ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    duration = fields.Integer(string='Duration', required=True, default=1)
    price = fields.Monetary(string='Price', required=True)
    unit = fields.Selection(
        [('day', 'Day(s)'), ('week', 'Week(s)'), ('month', 'Month(s)')],
        string='Unit', default='day', required=True
    )
    description = fields.Text(string='Description')
    sequence = fields.Integer(string='Sequence', default=10)

    # Relational -------
    currency_id = fields.Many2one(
        comodel_name='res.currency', string='Currency', required=True,
        default=lambda self: self.env.user.company_id.currency_id)
    motorcycle_model_id = fields.Many2one("mbr.motorcycle.model", string="Motorcycle model",
                                          required=True)

    # ----------------------------------- Constrains and Onchanges --------------------------------
    @api.constrains('unit', 'duration')
    def _check_duration(self):
        for record in self:
            if record.unit == 'day' and record.duration < 1 or record.duration > 6:
                raise ValidationError("Duration must be between 1 and 6!")
            if record.unit == 'week' and record.duration < 1 or record.duration > 3:
                raise ValidationError("Duration must be between 1 and 3!")
            if record.unit == 'month' and record.duration < 1:
                raise ValidationError("Duration must be greater than 0!")

    @api.constrains("price")
    def _check_price(self):
        # TODO: Work only when same currency
        # TODO: Price 1 week need to be greater than price 1 day
        # TODO: Price 1 month need to be greater than price 1 week
        # Price must be greater than 0
        for record in self:
            if record.price <= 0:
                raise ValidationError("Price must be greater than 0!")
        # Price must be increasing
        for unit in ('day', 'week', 'month'):
            price_duration_list = self.search([
                ('motorcycle_model_id', '=', self.motorcycle_model_id.id),
                ('unit', '=', unit),
            ]).mapped(lambda r: (r.duration, r.price))
            price_duration_list = sorted(price_duration_list, key=lambda x: x[0])
            for i in range(len(price_duration_list) - 1):
                if price_duration_list[i][1] >= price_duration_list[i + 1][1]:
                    raise ValidationError(f"Price by unit must be increasing by duration!")
