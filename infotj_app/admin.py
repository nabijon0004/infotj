from django.contrib import admin
from infotj_app.models import Establishment, EstablishmentPhoto, Photo


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):

    model = Establishment
    list_display = ('id', 'name', 'type_of_establishment', 'city')
    search_fields = ('name', 'address_street', 'city')
    list_per_page = 10
    


admin.site.register(EstablishmentPhoto)

admin.site.register(Photo)

