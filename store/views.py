from django.shortcuts import render, redirect
import rest_framework
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer


# Create your views here.
def store(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {'products': products}
        if request.user.is_authenticated:
            return render(request, 'store.html', context)
        else:
            return redirect('/signin/')


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self):
        pass