from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow


def index(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shops = Shop.objects.all()
    shophead = shops[0]  # 头部区块
    shoptab = shops[1:3]  # 长条数据
    shopclass = shops[3:7]  # 分类
    shopcommend = shops[7:11]  # 推荐
    mainlist = Mainshow.objects.all()
    date = {
        'title': '首页',
        'wheels': wheels,
        'navs': navs,
        'mustbuys': mustbuys,
        'shophead': shophead, 'shoptab': shoptab,
        'shopclass': shopclass, 'shopcommend': shopcommend,
        'mainlist': mainlist,
    }
    return render(request, 'index/index.html', context=date)


def cart(request):
    return render(request, 'cart/cart.html')


def market(request):
    return render(request, 'market/market.html')


def mine(request):
    return render(request, 'mine/mine.html')
