import logging

_logger = logging.getLogger(__name__)


def pre_init_hook(cr):
    """Pre-create receipt_status column to avoid a full recompute on install.

    receipt_status is a stored computed field on purchase.order.line. Installed
    over a populated table, _auto_init marks every existing row for
    recomputation (odoo/models.py:2657-2670, because field.update_db returns
    True when the column is missing, odoo/fields.py:1027). On ~110k lines this
    locks the table and blocks the upgrade.

    Creating the column beforehand makes update_db return False, so no mass
    recompute is queued; the field computes normally on later writes. Idempotent.
    """
    cr.execute(
        """
        ALTER TABLE purchase_order_line
        ADD COLUMN IF NOT EXISTS receipt_status varchar;
        """
    )
    _logger.info(
        "pre_init_hook: ensured purchase_order_line.receipt_status column exists"
    )
