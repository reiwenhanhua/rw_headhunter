# -*- coding: utf-8 -*-
from odoo import http

# class RwHeadhunter(http.Controller):
#     @http.route('/rw_headhunter/rw_headhunter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rw_headhunter/rw_headhunter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rw_headhunter.listing', {
#             'root': '/rw_headhunter/rw_headhunter',
#             'objects': http.request.env['rw_headhunter.rw_headhunter'].search([]),
#         })

#     @http.route('/rw_headhunter/rw_headhunter/objects/<model("rw_headhunter.rw_headhunter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rw_headhunter.object', {
#             'object': obj
#         })