# -*- coding: utf-8 -*-
import odoo.exceptions
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
    # TODO: delete this field
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        default=lambda self: self.env.user.company_id.currency_id,
        string='Currency',
        required=True
    )
    rental_ids = fields.One2many(comodel_name="mbr.rental", inverse_name="motorcycle_id",
                                 string="Rentals")

    def _is_available(self, rd_start, rd_end):
        """
        Check if the motor is available in the given range
        """
        # TODO: research if this is the best way to do this
        if len(self) > 1:
            raise odoo.exceptions.UserError("This method is not implemented for multiple records")
        for motor in self:
            rentals = [(r.date_start, r.date_end) for r in motor.rental_ids]
            len_rentals = len(rentals)
            if len_rentals == 0:
                return True
            if len_rentals == 1 and rd_start < rd_end < rentals[0][0]:
                return True
            for i in range(len(rentals)):
                cur_rental = rentals[i]
                next_rental = rentals[i + 1] if i + 1 < len(rentals) else None
                if next_rental:
                    if cur_rental[1] < rd_start < rd_end < next_rental[0]:
                        return True
                elif cur_rental[1] < rd_start < rd_end:
                    return True

    # ------------------------------------------ CRUD Methods -------------------------------------
    @api.model
    def create(self, vals):
        vals['name'] = self.env['ir.sequence'].next_by_code('mbr.motorcycle')
        return super(MbrMotorcycle, self).create(vals)
