from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES,STYLE_CHOICES
from django.contrib.auth.models import User


#ModelSerializer takes care of the above implementation including the create and update functions
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ('url','pk','highlight','owner','title', 'code', 'linenos', 'language', 'style')
    owner=serializers.ReadOnlyField(source='owner.username')
    highlight=serializers.HyperlinkedIdentityField(view_name='snippet-highlight',format='html')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets=serializers.HyperlinkedRelatedField(many=True,view_name='snippet-detail',read_only=True)

    class Meta:
        model=User
        fields=('url','pk','username','snippets')