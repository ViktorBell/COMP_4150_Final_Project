from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=128)

class ThreeDModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_model = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=512)
    file_path = models.CharField(max_length=512)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

class ModelTextureMaps(models.Model):
    model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    file_path = models.CharField(max_length=512)
    description = models.TextField()

class ModelTag(models.Model):
    model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    star_rating = models.FloatField()
    review_text = models.TextField()

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    platform = models.CharField(max_length=128 )
