from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
<<<<<<< HEAD

    def ready(self):
        import checkout.signals
=======
>>>>>>> 19cb9d9654655786429dc13334ba3523a1c87595
