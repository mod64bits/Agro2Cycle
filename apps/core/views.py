from django.shortcuts import render
from django.views.generic import TemplateView
from apps.products.models import TypeProduct, Product


class DashBoardView(TemplateView):
    template_name = 'core/dashBoard.html'
