from django.db import models
from django.conf import settings

class PostQuestion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("User"), on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

class PostAnswer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("User"), on_delete=models.CASCADE)
    question = models.ForeignKey(PostQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.answer