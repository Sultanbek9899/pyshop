
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status

from .serializers import UserUpdateSerializer, UserDetailSerializer, TestSerializer
from src.apps.account.models import User


# class UserUpdateView(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication, SessionAuthentication] 

#     def get(self, request):
#         user = request.user
#         serializer = UserDetailSerializer(instance=user)
#         return Response(serializer.data, status=200)

#     def put(self, request):
#         user = request.user
#         serializer = UserUpdateSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(serializer.errors, status=400)


class UserDetailUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


    def get_object(self):
        return self.request.user






# Product Queryset ---> Serializer ----> ProductListJson




class TestAPIView(APIView):
    

    def post(self,request):
        print("REQUEST POST PRINT",request.POST)
        serializer = TestSerializer(data=request.POST)
        if serializer.is_valid():
            return Response(
                data={"message":"Data is correct and received", "status":"ok"},
                status=status.HTTP_200_OK
                )
        return Response(
                data={
                    "message":"Data is not correct",
                    "status":"failed",
                    "errors":serializer.errors
                    },
                status=status.HTTP_400_BAD_REQUEST
                )


    def get(self,request):
        from datetime import datetime
        data = {
            "start_time": datetime.now(),
            "quantity": 10,
            "to_email": "admin@gmail.com",
            "text": "Hello from Backend"
        }
        serializer = TestSerializer(data=data)
        if serializer.is_valid():
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        print(serializer.err)
        raise ValueError("Data isnt correct!")