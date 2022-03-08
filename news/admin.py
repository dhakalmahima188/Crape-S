from attr import fields
from rangefilter.filters import DateRangeFilter, DateTimeRangeFilter
from django.contrib import admin


# Register your models here.
from .models import files, tableForm


# class filesInline(admin.TabularInline):
#     model = files


class filesTable(admin.ModelAdmin):
    model = files

    list_display = [
        'creation_date', 'section', 'institutiontype',
        'institution', 'category', 'title', 'url'
    ]

    list_filter = (
        ('creation_date', DateRangeFilter), 'section', 'institutiontype',
        'institution',  'title', )
    list_editable = ('section', 'institution', 'title', 'institutiontype')
    search_fields = ['section', 'institution', 'title', ]
    list_display_links = ['url']

    def pre(self, obj):
        pass


admin.site.register(files, filesTable)
admin.site.register(tableForm)
# admin.site.register(fileTable)
