from logging import Filter

from django.contrib import admin
from .models import Listing, UserSearches, FilterSelection, Events

# Register your models here.
admin.site.register(Listing)
admin.site.register(UserSearches)
admin.site.register(FilterSelection)
admin.site.register(Events)