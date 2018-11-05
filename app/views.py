import hashlib
import os
import uuid

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from AXF import settings
from app.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods, User


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
        goods_list = Goods.objects.filter(categoryid=categoryid)  # 商品数据
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


# 我的
def mine(request):
    token = request.COOKIES.get('token')
    responseData = {
        'name': '未登录',
        'rank': '',
        'img': '/static/uploads/uu.png'
    }
    if token:  # 登录
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img
    else:
        responseData = responseData
    return render(request, 'mine/mine.html', context=responseData)


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'mine/register.html')
    elif request.method == 'POST':
        user = User()
        user.account = request.POST.get('account')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('username')
        user.tel = request.POST.get('tel')
        user.address = request.POST.get('address')
        imgName = user.account + '.png'
        imgPath = os.path.join(settings.MEDIA_ROOT, imgName)
        file = request.FILES.get('img')
        with open(imgPath, 'wb') as fp:
            for data in file.chunks():
                fp.write(data)
        user.img = imgName
        user.token = uuid.uuid5(uuid.uuid4(), 'register')
        user.save()
        response = redirect('app:mine')
        response.set_cookie('token', user.token)
        return response


# 密码加密
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 验证账号
def checkaccount(request):
    account = request.GET.get('account')
    try:
        user = User.objects.get(account=account)
        return JsonResponse({'msg': '账号存在!', 'status': '0'})
    except:
        return JsonResponse({'msg': '账号可用!', 'status': '1'})

    # print(request.GET.get('account'))


def logout(request):
    response = redirect('app:mine')
    response.delete_cookie('token')
    return response


# 登录
def login(request):
    return render(request,'mine/login.html')