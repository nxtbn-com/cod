metadata = {
    "plugin_name": "code",
    "plugin_type": "PAYMENT_PROCESSOR",
    "plugin_uri": "https://github.com/nxtbn-com/cod",
    "version": "1.0.1",
    "author": "bytenyx limited",
    "author_uri": "http://bytenyx.com",
    "description": "Plugin to handle payment via cash on delivery.",
    "license": "BSD-3-Clause",
    "nxtbn_version_compatibility": ">=1.0.0",
    "has_urls": True,
    "environment_variables": {
        'STRIPE_SECRET_KEY': 'secret',
        'STRIPE_PUBLIC_KEY': 'str',
        'USE_STRIPE_INVOICE': 'bool'
    }
}

from . cash_on_delivery import CashOnDelivery

gateway = CashOnDelivery

__all__ = ['gateway']
