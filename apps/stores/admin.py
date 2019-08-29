from django.contrib import admin
from django.template.defaultfilters import slugify

from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'slug',
    )

    search_fields = (
        'name',
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if not request.user.is_superuser:
            queryset = queryset.filter(owner=request.user)

        return queryset

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser:
            obj.owner = request.user
            obj.slug = slugify(obj.name)

        super(StoreAdmin, self).save_model(request, obj, form, change)

    def get_prepopulated_fields(self, request, obj=None):
        if request.user.is_superuser:
            prepopulated_fields = {'slug': (
                'name',
            )}

        else:
            prepopulated_fields = self.prepopulated_fields

        return prepopulated_fields

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            fieldsets = (
                (None, {'fields': (
                    'owner',
                    'name',
                    'slug',
                    'description',
                )}),
            )

        else:
            fieldsets = (
                (None, {'fields': (
                    'name',
                    'description',
                )}),
            )

        return fieldsets

    def get_list_filter(self, request):
        if request.user.is_superuser:
            list_filter = (
                'owner',
            )

        else:
            list_filter = self.list_filter

        return list_filter


admin.site.register(Store, StoreAdmin)
