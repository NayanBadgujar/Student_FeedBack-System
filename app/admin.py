from django.contrib import admin
from .models import Feedback
from .models import Contact
# Register your models here.
admin.site.register(Feedback)
admin.site.register(Contact)