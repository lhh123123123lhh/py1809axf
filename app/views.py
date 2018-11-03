from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


# 首页
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


# 闪购超市
def market(request, categoryid, childid, sortid):
    type_list = Foodtypes.objects.all()  # 分类数据

    # 子类数据
    typeIndex = int(request.COOKIES.get('typeIndex', 0))
    childtypenames = type_list[typeIndex].childtypenames
    categoryid = type_list[typeIndex].typeid
    childtypeList = []
    for str1 in childtypenames.split('#'):
        str2 = str1.split(':')
        obj = {'childname': str2[0], 'childid': str2[1]}
        childtypeList.append(obj)

    if childid == '0':
        goods_list = Goods.objects.filter(categoryid=categoryid)# 商品数据
    else:
        goods_list = Goods.objects.filter(categoryid=categoryid, childcid=childid)

    if sortid == '2':
        goods_list = goods_list.order_by('productnum')
    elif sortid == '3':
        goods_list = goods_list.order_by('price')
    elif sortid == '4':
        goods_list = goods_list.order_by('-price')
    date = {
        'type_list': type_list,
        'goods_list': goods_list,
        'childtypeList': childtypeList,
        'categoryid': categoryid,
        'childid': childid,
    }
    return render(request, 'market/market.html', context=date)


def mine(request):
    return render(request, 'mine/mine.html')
