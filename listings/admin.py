from django.contrib import admin
from .models import Listing
from .forms import PoisForm
from .models import Poi


class PoiAdmin(admin.ModelAdmin):
    form = PoisForm


admin.site.register(Listing)
admin.site.register(Poi, PoiAdmin)
