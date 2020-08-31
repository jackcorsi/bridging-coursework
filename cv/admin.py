from django.contrib import admin
from .models import ContactDetail
from .models import Institution
from .models import Qualification
from .models import Skill
from .models import Experience


# Register your models here.
admin.site.register(ContactDetail)


class QualificationInline(admin.StackedInline):
    model = Qualification
    extra = 1


class InstitutionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["name", "additional_info", "start_date", "end_date"]})]
    inlines = [QualificationInline]


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Qualification)
admin.site.register(Skill)
admin.site.register(Experience)

