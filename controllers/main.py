from openerp.addons.auth_signup.controllers.main import AuthSignupHome
from odoo import http, _
from odoo.exceptions import UserError
from odoo.http import request


class AuthCaptcha(AuthSignupHome):

    @http.route()
    def web_login(self, *args, **kw):
        """ Inherited web_login() from the auth_signup base model for adding
            validation of captcha code in login screen.

               :param *args: default argument of the web_login().
               :param **kw : represent all key values of login response.
               :returns: object of super method of auth_signup model's base class.
        """
        request.params['login_success'] = False

        if request.httprequest.method == 'POST':

            if request.params.get('g-recaptcha-response') == '':
                # raise UserError(_("Captcha code is necessary."))
                request.params['login_success'] = False
                return http.redirect_with_hash(request.params.get('redirect'))

            else:
                request.params['login_success'] = True

        response = super(AuthSignupHome, self).web_login(*args, **kw)
        response.qcontext.update(self.get_auth_signup_config())
        if request.httprequest.method == 'GET' and request.session.uid and request.params.get('redirect'):
            # Redirect if already logged in and redirect param is present
            return http.redirect_with_hash(request.params.get('redirect'))
        return response

    def do_signup(self, qcontext):

        """ Inherited do_signup() from the auth_signup base model for adding validation of
            captcha code in signup screen.

                       :param qcontext : represent all key values of signup response.
                       :returns: object of super method of auth_signup model's base class.
                """

        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'g-recaptcha-response')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        if values.get('g-recaptcha-response') == '':
            raise UserError(_("Captcha code is necessary."))
        res = super(AuthCaptcha, self).do_signup(qcontext)
        return res
        request.env.cr.commit()