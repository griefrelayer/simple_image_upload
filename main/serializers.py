from rest_framework import serializers
from .models import MyImage
from PIL import Image


class MyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = ('file', 'uploaded_at')

    def create(self, validated_data):
        image_file = validated_data['file']
        im = Image.open(image_file)
        im = im.resize((800, 800), Image.ANTIALIAS)
        im = im.rotate(180)
        image_file.seek(0)
        image_file.size = 800, 800
        im.save(image_file, "jpeg")
        image_file.seek(0)
        return super().create(validated_data)
