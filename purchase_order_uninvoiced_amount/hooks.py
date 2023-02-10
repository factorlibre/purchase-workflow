# © 2023 - FactorLibre - Oscar Indias <oscar.indias@factorlibre.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

def pre_init_hook(cr):
    cr.execute(
        """ALTER TABLE purchase_order
        ADD COLUMN IF NOT EXISTS amount_uninvoiced numeric DEFAULT 0.0"""
    )
