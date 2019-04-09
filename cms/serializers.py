from rest_framework import serializers
from cms.models import Book


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'id', 'name', 'publisher', 'page')
