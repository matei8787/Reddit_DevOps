from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Bug

class BugSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    
    class Meta:
        model = Bug
        fields = ['title', 'description', 'created_at', 'updated_at', 'score', 'upvotes', 'downvotes']
        read_only_fields = ['created_at', 'updated_at', 'score', 'upvotes', 'downvotes']
        
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def validate_title(self, data):
        data = data.strip()
        return data
    
    