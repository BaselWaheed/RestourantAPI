from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ReservationSerializer , CommentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated   
from rest_framework.views import APIView
from .models import Reservation , Comment
from authentication.views import GuestAuthentication, TokenAuthentication
import pickle


class ReservationAPI(APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication,)
    def post(self, request):
        data = {"info":[]}
        massege = 'The booking has been successfully registered and is awaiting approval'
        reservationSerializer = ReservationSerializer(data=request.data)
        if reservationSerializer.is_valid():
            reservationSerializer.save(user=self.request.user)
            data['info'].append(reservationSerializer.data)  
            return Response({'status': True,'massege': massege,'data': data } ,status=status.HTTP_201_CREATED)
        return Response({'status': False,'data': []}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request , **kwargs):
        data = {"info":[]}
        reservation = Reservation.objects.filter(user=self.request.user)
        if reservation:
            reservationSerializer = ReservationSerializer(reservation , many = True)
            for info in reservationSerializer.data:
                data['info'].append(info)
            return Response({'status': True,'message' :'your Reservation ','data': data} ,status=status.HTTP_200_OK)
        else :
            return Response({ 'status' : True ,'message' :'No Reservation found','data':data},status=status.HTTP_404_NOT_FOUND)

'''
loads vectorizer to make the bag of words 
loads the model to predict the input
variable X transform the comment and make bag of words 
variable y_pred has the classifier and predict the sentiment of the comment 
'''
def analyzer(comment):
    try:
        model = pickle.load(open(r"C:\Users\GIG\Desktop\LOL\project\staff\model.pkl","rb"))
        cv = pickle.load(open(r"C:\Users\GIG\Desktop\LOL\project\staff\cv.pkl","rb"))
        X = cv.transform([comment])
        y_pred = model.predict(X)
        print(y_pred)
        return y_pred
    except ValueError as e: 
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST) 



def managecomment(request):
    if request.method == 'GET':
        model = pickle.load(open('model.pkl', 'rb'))
        cv = pickle.load(open('cv.pkl', 'rb'))
        comments = Comment.objects.filter(comm_is_managed=False)
        for comment in comments:
            X = cv.transform([comment.comment])
            y_pred = model.predict(X)
            if y_pred == 0 :
                comment.comm_sentiment = False
            else :
                comment.comm_sentiment = True
            
            comment.comm_is_managed = True
            comment.save()

    number_comment = Comment.objects.all().count()
    comment_accept = Comment.objects.filter(comm_sentiment=True).count()
    comment_rejected = comment_accept - number_comment
    context = {'comments':comments, 'comment_accept':comment_accept,'comment_rejected':comment_rejected ,'number_comment':number_comment}
    return render(request,'comments.html',context)
        


class CommentAPI(APIView):
    authentication_classes = (TokenAuthentication,GuestAuthentication)
    permission_classes = [IsAuthenticated,]     
    def post(self, request): 

        Serializer = CommentSerializer(data=request.data,context={"request":request})
        data = {"info":[]}
        if Serializer.is_valid():
            Serializer.save()
            data['info'].append(Serializer.data) 
            return Response({'status': True,'massege':'Your Review is Done' ,'data': data } ,status=status.HTTP_201_CREATED)
        else :
            return Response({'status': False,'data': data}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request,**kwargs):
        comment = Comment.objects.filter(comm_is_shown=True)
        data = {"info":[]}
        if comment :
            commentserializer = CommentSerializer(comment , many=True)
            for info in commentserializer.data :
                data['info'].append(info)
            return Response({'status': True,'message':' working','data': data} ,status=status.HTTP_200_OK)
        else :
            return Response({'status': True,'message':'No Review available','data': data} ,status=status.HTTP_200_OK)






