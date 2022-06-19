
from django.shortcuts import get_object_or_404
from .models import Category, Dish
from rest_framework.response import Response
from .serializer import DishSerializer , CategorySerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from order.models import  Order
from rest_framework.generics import  ListCreateAPIView
from authentication.views import  GuestAuthentication


class CategoryVIEW(APIView):
    def get(self,request):
        query = Category.objects.all()
        serializers = CategorySerializer(query, many=True)
        return Response({'status':True , 'messege' : 'anta kda tmam' , 'data':serializers.data},status=status.HTTP_200_OK)



class MeetDishVIEW(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        query = Dish.objects.filter(dish_category='17528fdf-c099-43a7-809b-58988d035148')
        data = {'product':[]}
        serializers = DishSerializer(query, many=True ,context={"request":request})
        for product in serializers.data :
            # try :
            #     obj = FavouriteDish.objects.filter(user=self.request.user).filter(product_id=product['id'])
            #     pro = Order.objects.filter(user=self.request.user).filter(order_contain=product['id'])
            #     if obj  :
            #         data['is_favourite'] = obj[0].is_favourite
            #     else :
            #         data['is_favourite'] = False
            #     if pro :
            #         data['in_cart'] = True
            #     else :
            #         data['in_cart'] = False
            # except :
            #     data['is_favourite'] = False
            #     data['in_cart'] = False  
            data["product"].append(product)
        return Response({'status':True , 'messege' : 'done' , 'data':data},status=status.HTTP_200_OK)

class DrinksDishVIEW(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        query = Dish.objects.filter(dish_category='253cfa6e-88ae-492e-9c8a-0d1be210d79a')
        data = {'product':[]}
        serializers = DishSerializer(query, many=True , context={"request":request})
        for product in serializers.data :
            # try :
            #     obj = FavouriteDish.objects.filter(user=self.request.user).filter(product_id=product['id'])
            #     pro = Order.objects.filter(user=self.request.user).filter(order_contain=product['id'])
            #     if obj  :
            #         data['is_favourite'] = obj[0].is_favourite
            #     else :
            #         data['is_favourite'] = False
            #     if pro :
            #         data['in_cart'] = True
            #     else :
            #         data['in_cart'] = False
            # except :
            #     data['is_favourite'] = False
            #     data['in_cart'] = False  
            data["product"].append(product)
        return Response({'status':True , 'messege' : 'done' , 'data':data},status=status.HTTP_200_OK)
class VegetablesDishVIEW(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        query = Dish.objects.filter(dish_category='d8168acd-956f-4a04-87f5-842008e6f35d')
        data = {'product':[]}
        serializers = DishSerializer(query, many=True,context={"request":request})
        for product in serializers.data :
            # try :
            #     obj = FavouriteDish.objects.filter(user=self.request.user).filter(product_id=product['id'])
            #     pro = Order.objects.filter(user=self.request.user).filter(order_contain=product['id'])
            #     if obj  :
            #         data['is_favourite'] = obj[0].is_favourite
            #     else :
            #         data['is_favourite'] = False
            #     if pro :
            #         data['in_cart'] = True
            #     else :
            #         data['in_cart'] = False
            # except :
            #     data['is_favourite'] = False
            #     data['in_cart'] = False  
            data["product"].append(product)
        return Response({'status':True , 'messege' : 'done' , 'data':data},status=status.HTTP_200_OK)

class ChickenDishVIEW(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        query = Dish.objects.filter(dish_category='1e0b178c-8aa1-4a21-8782-55582ae4a8d1')
        data = {'product':[]}
        serializers = DishSerializer(query, many=True,context={"request":request})
        for product in serializers.data :
            # try :
            #     obj = FavouriteDish.objects.filter(user=self.request.user).filter(product_id=product['id'])
            #     pro = Order.objects.filter(user=self.request.user).filter(order_contain=product['id'])
            #     if obj  :
            #         data['is_favourite'] = obj[0].is_favourite
            #     else :
            #         data['is_favourite'] = False
            #     if pro :
            #         data['in_cart'] = True
            #     else :
            #         data['in_cart'] = False
            # except :
            #     data['is_favourite'] = False
            #     data['in_cart'] = False  
            data["product"].append(product)
        return Response({'status':True , 'messege' : 'done' , 'data':data},status=status.HTTP_200_OK)

class DishDetailsView(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)

    def post(self,request):
        product = get_object_or_404(Dish, pk=request.data.get('id'))
        serializer = DishSerializer(product,context={"request":request})
        return Response({'status': True,'data':serializer.data} ,status=status.HTTP_200_OK)



class HomeDishView(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        query = Dish.objects.filter(is_active= True)
        data = {'product':[]}
        serializers = DishSerializer(query, many=True,context={"request":request})
        for product in serializers.data :
            data["product"].append(product)
        return Response({'status':True , 'messege' : 'done' , 'data':data},status=status.HTTP_200_OK)



# class SearchAPI(ListAPIView):
    # authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#     filter_backends = [DjangoFilterBackend ,filters.SearchFilter]
#     filterset_fields = ['id','dish_name']
#     search_fields = ['dish_name']
#     def list(self, request, *args, **kwargs):
#         data = {}
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             data['product']=serializer.data
#             return self.get_paginated_response({'status': True,'data':data})
#         serializer = self.get_serializer(queryset, many=True)
#         data['product']=serializer.data
#         return Response({'status': True,'data':data})
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class SearchAPI(ListAPIView):
    # authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)
#     queryset = Dish.objects.all()
#     serializer_class = DishSerializer
#     def list(self, request, *args, **kwargs):
#         data = {}
#         queryset = self.filter_queryset(self.get_queryset())
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             data['product']=serializer.data
#             return self.get_paginated_response({'status': True,'data':data})
#         serializer = self.get_serializer(queryset, many=True)
#         data['product']=serializer.data
#         return Response({'status': True,'data':data})
#     def get(self, request, *args, **kwargs):
#         print(self.request.data)
#         SearchAPI.queryset = Dish.objects.filter(dish_name__contains=request.data['dish_name'])
#         return self.list(request, *args, **kwargs)


class SearchAPI(ListCreateAPIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    def list(self, request, *args, **kwargs):
        data = {}
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True ,context={"request":request})
            data['product']=serializer.data
            return self.get_paginated_response({'status': True,'data':data})
        serializer = self.get_serializer(queryset, many=True,context={"request":request})
        data['product']=serializer.data
        return Response({'status': True,'data':data})
    def post(self, request, *args, **kwargs):
        SearchAPI.queryset = Dish.objects.filter(dish_name__contains=request.data['dish_name'])
        return self.list(request, *args, **kwargs)
    def get(self, request, *args, **kwargs):
        return Response({'status':False , "message":"method GET not allowed"})




# advanced category 


class CategoryMobileAndWebViewAPI(APIView):
    authentication_classes = (GuestAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request):
        data = {"homepage":[],"category":[]}
        products = {'product':[]}
        category = Category.objects.all()
        category_serializer= CategorySerializer(category,many=True)
        for item in category_serializer.data :
            category = Category.objects.get(cat_name=item['cat_name'])
            categoryfilter = Dish.objects.filter(dish_category=category.id)
            serializer = DishSerializer(categoryfilter,many=True,context={"request":request})
            for product in serializer.data :
                # try :
                #     obj = FavouriteDish.objects.filter(user=self.request.user).filter(product_id=product['id'])
                #     pro = Order.objects.filter(user=self.request.user).filter(order_contain=product['id'])
                #     if obj  :
                #         product['is_favourite'] = obj[0].is_favourite
                #     else :
                #         product['is_favourite'] = False
                #     if pro :
                #         product['in_cart'] = True
                #     else :
                #         product['in_cart'] = False
                # except :
                #     product['is_favourite'] = False
                #     product['in_cart'] = False
                if product['is_active']==True :
                    data['homepage'].append(product)  
                products['product'].append(product)
            item['products']=products  
            data['category'].append(item)
            products = {'product':[]} 
        return Response({"status":True , "message":"working", "data": data}, status=status.HTTP_200_OK)     

# class CategoryWebViewAPI(APIView):
#     permission_classes = (AllowAny,)
#     def get(self,request):
#         data = {"category":[]}
#         products = {'product':[]}
#         category = Category.objects.all()
#         category_serializer= CategorySerializer(category,many=True)
#         for item in category_serializer.data :
#             category = Category.objects.get(cat_name=item['cat_name'])
#             categoryfilter = Dish.objects.filter(dish_category=category.id)
#             serializer = DishSerializer(categoryfilter,many=True)
#             for product in serializer.data :
#                 product['is_favourite'] = False
#                 product['in_cart'] = False
#                 products['product'].append(product)
#             data['category'].append(item)
#             item['products']=product
#         return Response({"status":True , "message":"working", "data": data}, status=status.HTTP_200_OK) 

