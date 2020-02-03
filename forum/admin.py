from django.contrib import admin
from .models import PostAnswer, PostQuestion
# Register your models here.
admin.site.register(PostQuestion)
admin.site.register(PostAnswer)