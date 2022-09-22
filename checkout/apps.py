from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Checkout configuration
    """
    name = 'checkout'

    def ready(self):
        import checkout.signals
