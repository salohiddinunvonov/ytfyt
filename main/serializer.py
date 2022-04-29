from rest_framework import serializers
from .models import *



class SerializerBook(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class SerializerAudioBook(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = "__all__"


class SerializerCategory(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SerializerLanguage(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SerializerHistoryBook(serializers.ModelSerializer):
    class Meta:
        model = HistoryBook
        fields = "__all__"


class SerializerHistoryAudioBook(serializers.ModelSerializer):
    class Meta:
        model = HistoryAudioBook
        fields = "__all__"

class SerializerRatingAudioBook(serializers.ModelSerializer):
    class Meta:
        model = RatingAudioBook
        fields = "__all__"

class SerializerRatingBook(serializers.ModelSerializer):
    class Meta:
        model = RatingBook
        fields = "__all__"
