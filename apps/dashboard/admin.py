from django.contrib import admin
from .models import Contact,SocialMedia,Skill,Interent,Resume,DetailItem,DetailResume
# Register your models here.
admin.site.register(Contact)
admin.site.register(SocialMedia)
admin.site.register(Skill)
admin.site.register(Interent)
admin.site.register(Resume)
admin.site.register(DetailItem)
admin.site.register(DetailResume)
