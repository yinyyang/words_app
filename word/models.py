from django.db import models

# Create your models here.


class Word(models.Model):
    youdao = models.TextField()
    english= models.TextField()


    def __str__(self):
        return  "%s |  %s " % (
            self.english,
            self.youdao,
        )

