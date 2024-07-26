# -*- coding: utf-8 -*-
# from odoo import http


# class DhDeliverynoteProductpackTotal(http.Controller):
#     @http.route('/dh_deliverynote_productpack_total/dh_deliverynote_productpack_total/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dh_deliverynote_productpack_total/dh_deliverynote_productpack_total/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dh_deliverynote_productpack_total.listing', {
#             'root': '/dh_deliverynote_productpack_total/dh_deliverynote_productpack_total',
#             'objects': http.request.env['dh_deliverynote_productpack_total.dh_deliverynote_productpack_total'].search([]),
#         })

#     @http.route('/dh_deliverynote_productpack_total/dh_deliverynote_productpack_total/objects/<model("dh_deliverynote_productpack_total.dh_deliverynote_productpack_total"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dh_deliverynote_productpack_total.object', {
#             'object': obj
#         })
