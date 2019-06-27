from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    has_google_recaptcha = fields.Boolean(readonly=False)

    @api.onchange('has_google_recaptcha')
    def on_change_state(self):
        for record in self:
            self.has_google_recaptcha == True
