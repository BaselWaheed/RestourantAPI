from rest_framework import serializers

from Auth.models import User
from .models import Comment , Reservation




class ReservationSerializer(serializers.ModelSerializer):
    res_time = serializers.TimeField(format='%I:%M %p',input_formats=["%I:%M %p",'%H:%M'])
    class Meta :
        model = Reservation
        fields = ['id','res_date' , 'res_guest_count' , 'res_time' ,'res_is_confermed' ]




class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self,obj):
        try :
            user = User.objects.get(email=obj)
            user = user.username
            
        except :
            user = "No name "
        return user
        

    class Meta :
        model = Comment
        fields = ['user','comment']

    def save(self,**kwargs):
        comment=Comment(
            user=self.context['request'].user,
            comment=self.validated_data['comment'],
        )
        comment.save()
        return comment