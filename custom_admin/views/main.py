from django.contrib.admin import util as django_admin_util
import django.contrib.admin.views.main
from django.core.urlresolvers import reverse


class LinkToDetailChangelist(django.contrib.admin.views.main.ChangeList):

    def url_for_result(self, result):
        """Return the URL for a ``result`` in the changelist.

        Based in the overriden method of Django 1.6 but returns the URL for
        the detail view (``'admin:%s_%s_detail'``) instead of the
        change view (``'admin:%s_%s_change'``).

        """
        pk = getattr(result, self.pk_attname)
        info = self.opts.app_label, self.opts.module_name
        # TODO: replace `module_name` with `model_name` when using Django 1.6

        return reverse('admin:%s_%s_detail' % info,
                       args=(django_admin_util.quote(pk), ),
                       current_app=self.model_admin.admin_site.name)
