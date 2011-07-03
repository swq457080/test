from django.contrib import admin
from models import License, Submission, Revision

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('sub_type', 'slug', 'created_by', 'num_revisions',
                    'is_displayed',)

class RevisionAdmin(admin.ModelAdmin):
    list_display = ('entry', 'created_by', 'sub_license', 'item_url')

admin.site.register(License, LicenseAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Revision, RevisionAdmin)