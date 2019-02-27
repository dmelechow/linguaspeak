from django.contrib import admin
from .models import LinguaLevel
from .models import Language
from .models import Thread

# Register your models here.
admin.site.register(LinguaLevel)
admin.site.register(Language)
admin.site.register(Thread)
