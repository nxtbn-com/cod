metadata = {
    "plugin_name": "code",
    "plugin_type": "PAYMENT_PROCESSOR",
    "plugin_uri": "https://github.com/nxtbn-com/cod",
    "version": "1.0.1",
    "author": "bytenyx limited",
    "author_uri": "http://bytenyx.com",
    "description": "Plugin to handle payment via cash on delivery.",
    "license": "BSD-3-Clause",
    "nxtbn_version_compatibility": ">=1.0.0"
}

from . cash_on_delivery import CashOnDelivery

gateway = CashOnDelivery

__all__ = ['gateway']
