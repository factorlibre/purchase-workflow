# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Janire Olagibel
#    Copyright 2016 FactorLibre
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Purchase Stock on order lines',
    'summary': """Shows real and virtual stock
        for the product in purchase order lines""",
    'version': '0.1',
    'author': "FactorLibre,Odoo Community Association (OCA)",
    'category': 'Purchases Management',
    'license': 'AGPL-3',
    'images': [],
    'website': "http://factorlibre.com",
    'depends': [
        'purchase', 'stock'
    ],
    'data': [
        'view/purchase_view.xml'
    ],
    'installable': True,
}
