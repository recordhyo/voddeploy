from django.db import models

class Vod(models.Model):
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(max_length=500, null=True)
    bigcategory = models.CharField(max_length=50, null=False,default="기타")
    smallcategory = models.CharField(max_length=50, null=False,default='기타')
    category = models.CharField(max_length=50, null=True)
    actors = models.CharField(max_length=200, null=True)
    director = models.CharField(max_length=50, null=True)
    runningtime = models.CharField(max_length=10,null=True)
    imgpath = models.CharField(max_length=100, null=True)
    name_no_space = models.CharField(max_length=255,editable=False)
    backgroundimgpath=models.CharField(max_length=100,null=True)

    def save(self, *args, **kwargs):
        self.name_no_space = self.name.replace(' ', '')
        super(Vod, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name