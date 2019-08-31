from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Category


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (
            'name',
            'slug',
            'description',
        )}),
    )

    list_display = (
        'name',
        'slug',
    )

    prepopulated_fields = {
        'slug': (
            'name',
        ),
    }

    search_fields = (
        'name',
    )

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.slug = slugify(obj.name)

        super(CategoryAdmin, self).save_model(request, obj, form, change)


admin.site.register(Category, CategoryAdmin)
