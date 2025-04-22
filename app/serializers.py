from dataclasses import fields
from rest_framework import serializers
from .models import Competition, Entry, EntryImage
from rest_framework.serializers import ModelSerializer

class CompetitionListSerializer(ModelSerializer):
    class Meta:
        model = Competition
        fields = "__all__"


class EntryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryImage
        fields = ['image']


class EntryListSerializer(serializers.ModelSerializer):
    images = EntryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = [
            'id', 'full_name', 'email', 'phone', 'age', 'Location', 'theme_of_entry',
            'description', 'photography_experience', 'profile_picture',
            'instagram_username', 'competition', 'images', 'vote_count'
        ]


class EntryVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = ["id", "vote_count"]

class VoteSubmissionSerializer(serializers.Serializer):
    vote_count = serializers.IntegerField(min_value=4)