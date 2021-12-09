''' Checkout signals '''
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ Override default checkout signal """
    name = 'checkout'

    def ready(self):
        import checkout.signals
