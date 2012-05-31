# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import SimpleListFilter

class DecadeBornListFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('tyep')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1', _('in the eighties')),
            ('2', _('in the nineties')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(1)#(type__gte(1), type__lte(1))
        if self.value() == '2':
            return queryset.filter(1)#(type__gte(2), type__lte(2))
