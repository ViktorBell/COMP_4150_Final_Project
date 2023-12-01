from rest_framework import serializers
from .models import ThreeDModel, ModelTextureMap, Review, Share, Tag

class ThreeDModelSerializer(serializers.ModelSerializer):
    auxiliary_models = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ThreeDModel
        fields = ['id', 'user', 'name', 'file_path', 'description', 'likes', 'shares', 'main_model']

class ModelTextureMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTextureMap
        fields = ['id', 'model', 'file_path']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'model', 'user', 'comment', 'rating', 'created_at']

class ShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Share
        fields = ['id', 'model', 'user', 'shared_on']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
