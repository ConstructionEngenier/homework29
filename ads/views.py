import json

import pandas
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


class AddAdsData(View):
    def get(self, request):
        data_ads = pandas.read_csv('/Users/artem/Artems documents/Python/lesson27/homework27/data/ad.csv', sep=',').to_dict()

        i = 0
        while max(data_ads['Id'].keys()) > i:
            ad = Ad.objects.create(
                name=data_ads["name"][i],
                author=data_ads["author"][i],
                price=int(data_ads["price"][i]),
                description=data_ads["description"][i],
                address=data_ads["address"][i],
                is_published=data_ads["is_published"][i],
            )
            i += 1
        return JsonResponse("Data upload successful", safe=False, status=200)


class AddCatData(View):
    def get(self, request):
        data_cat = pandas.read_csv('/Users/artem/Artems documents/Python/lesson27/homework27/data/category.csv',
                                   sep=',').to_dict()

        i = 0
        while max(data_cat['id'].keys()) > i:
            cat = Category.objects.create(
                name=data_cat["name"][i],
            )
            i += 1
        return JsonResponse("Data upload successful", safe=False, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdView(View):

    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            price=ad_data["price"],
            description=ad_data["description"],
            address=ad_data["address"],
            is_published=ad_data["is_published"],
        )
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.adress,
            "is_published": ad.is_published,
        }, safe=False)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryView(View):

    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False)

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category.objects.create(
            name=category_data["name"]
        )
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, safe=False)


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        })


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })





