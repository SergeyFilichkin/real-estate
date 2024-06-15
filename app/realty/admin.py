from django.contrib import admin

from realty.models.flat import Flat

from realty.models.floor import Floor


class FlatAdmin(admin.ModelAdmin):
    list_display = (
        "price",
        "status",
        "category",
        "square",
        "rooms",
        "living_space",
        "kitchen_area",
    )

    search_fields = ("price", "category")

    list_filter = (
        "status",
        ("category", admin.RelatedFieldListFilter),
        "rooms",
    )

    list_editable = ("status",)


admin.site.register(Flat, FlatAdmin)


class FloorAdmin(admin.ModelAdmin):
    list_display = [
        "name"
    ]


admin.site.register(Floor, FloorAdmin)