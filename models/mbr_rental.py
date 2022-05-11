# -*- coding: utf-8 -*-

from odoo import fields, models, api


class MbrRental(models.Model):
    # ---------------------------------------- Private Attributes ---------------------------------

    _name = "mbr.rental"
    _description = "Motorcycle Rental"
    _sql_constraints = [
        ('mbr_discount_range',
         'CHECK (discount >= 0 AND discount <= 100)',
         'Discount must be between 0 and 100'),
    ]

    # --------------------------------------- Fields Declaration ----------------------------------

    # Basic -------
    name = fields.Char(string='Rental ID', required=True)
    discount = fields.Float(string='Discount', default=0.0)
    date_start = fields.Date(string='Start Date')
    date_end = fields.Date(string='End Date')
    # total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount')

    state = fields.Selection(
        string='Stage',
        selection=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('in_progress', 'In Progress'),
            ('done', 'Done'),
            ('canceled', 'Canceled'),
        ],
        default='draft',
        required=True,
        group_expand='_group_expand_states'
    )

    def _group_expand_states(self, states, domain, order):
        return [key for key, val in type(self).state.selection]

    customer_id = fields.Many2one('mbr.customer', string='Customer')
    motorcycle_id = fields.Many2one('mbr.motorcycle', string='Motorcycle')

    # def _compute_total_amount(self):
    #     for record in self:
    #         record.total_amount = record.motorcycle_id.price * (1 - record.discount / 100)
    #

    # ----------------------------------- Constrains and Onchanges --------------------------------
    @api.constrains('date_start', 'date_end')
    def _constrain_data_range(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_start > record.date_end:
                    raise models.ValidationError("Start date must be less than end date")
