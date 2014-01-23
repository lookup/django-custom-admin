import django.contrib.admin.forms
import django.contrib.auth.forms


class AdminCustomAuthForm(django.contrib.admin.forms.AdminAuthenticationForm):

    """Custom admin.forms.AdminAuthenticationForm that "replaces"
    :meth:`clean` with the one from its superclass
    auth.forms.AuthenticationForm.

    The purpose is to remove references to ``user.is_staff``.

    """

    def clean(self):
        return django.contrib.auth.forms.AuthenticationForm.clean(self)
