from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class AccountActivationGenerator(PasswordResetTokenGenerator):
    def _make_hash_values(self, user, timestamp):
        return(
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )

account_activation_code = AccountActivationGenerator()
