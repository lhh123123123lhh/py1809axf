from django.db import models


# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    trackid = models.CharField(max_length=10)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


class Nav(Base):
    class Meta:
        db_table = 'axf_nav'


class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


class Shop(Base):
    class Meta:
        db_table = 'axf_shop'


class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    isDelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'axf_mainshow'


class Foodtypes(models.Model):
    # 分类id
    typeid = models.CharField(max_length=10)
    # 分类名称
    typename = models.CharField(max_length=100)
    # 子类名称
    childtypenames = models.CharField(max_length=200)
    # 分类排序(显示的先后顺序)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'


class Goods(models.Model):
    # 商品ID
    productid = models.CharField(max_length=10)
    # 商品图片
    productimg = models.CharField(max_length=200)
    # 商品名称
    productname = models.CharField(max_length=100)
    # 商品长名字
    productlongname = models.CharField(max_length=200)
    # 精选
    isxf = models.BooleanField(default=False)
    # 买一送一
    pmdesc = models.BooleanField(default=False)
    # 规格
    specifics = models.CharField(max_length=100)
    # 价格
    price = models.FloatField()
    # 超市价格
    marketprice = models.FloatField()
    # 分类ID
    categoryid = models.CharField(max_length=10)
    # 子类ID
    childcid = models.CharField(max_length=10)
    # 子类名字
    childcidname = models.CharField(max_length=50)
    # 详情id
    dealerid = models.CharField(max_length=10)
    # 库存量
    storenums = models.IntegerField()
    # 销售量
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


class User(models.Model):
    # 账号
    account = models.CharField(max_length=20, unique=True)
    # 密码
    password = models.CharField(max_length=256)
    # 用户名
    name = models.CharField(max_length=50)
    # 手机号
    tel = models.CharField(max_length=20, unique=True)
    # 地址
    address = models.CharField(max_length=100)
    # 图片
    img = models.CharField(max_length=50)
    # 等级
    rank = models.CharField(max_length=10, default=1)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'axf_user'
