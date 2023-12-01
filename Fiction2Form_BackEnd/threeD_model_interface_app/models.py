from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

# Model for 3D Models
class ThreeDModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file_path = models.FileField(upload_to='models/')
    description = models.TextField(blank=True)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    main_model = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliary_models')

    def __str__(self):
        return self.name
# Model for Texture/Maps associated with 3D Models
class ModelTextureMap(models.Model):
    model = models.ForeignKey(ThreeDModel, related_name='textures', on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='textures/')

    def __str__(self):
        return f"Texture for {self.model.name}"

# Model for Reviews
class Review(models.Model):
    model = models.ForeignKey(ThreeDModel, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user} on {self.model.name}"

# Model for Shares
class Share(models.Model):
    model = models.ForeignKey(ThreeDModel, related_name='shares', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shared_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Share by {self.user} on {self.model.name}"

# Model for Tags
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Association between 3D Models and Tags
class ModelTag(models.Model):
    model = models.ForeignKey(ThreeDModel, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('model', 'tag')

    def __str__(self):
        return f"{self.tag.name} on {self.model.name}"

