# -*- coding: utf-8 -*-
from django.db import models
from constants import parking_lot_type

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length = 200)
    point = models.IntegerField()
    joined_time = models.DateTimeField('date joined', auto_now_add = True)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = '停车场用户'


class ParkingLot(models.Model):
    name = models.CharField(max_length = 400, verbose_name="停车场名称")
    address = models.CharField(max_length = 1000, verbose_name = "地址")
    type = models.IntegerField(verbose_name = "类型")
    latitude = models.FloatField(verbose_name = "纬度")
    longitude = models.FloatField(verbose_name = "经度")
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def parking_lot_type_str(self):
        return parking_lot_type[self.type]
    parking_lot_type_str.admin_order_field = 'type'
    parking_lot_type_str.short_description = '停车场类型'

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name_plural = '停车场'


class ParkingLotUser(models.Model):
    fk_user_id = models.ForeignKey(User, db_column = 'fk_user_id')
    fk_parking_lot_id = models.ForeignKey(ParkingLot, db_column = 'fk_parking_lot_id')
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)



class ParkingLotExtra(models.Model):
    fk_parking_lot_id = models.ForeignKey(ParkingLot, db_column = 'fk_parking_lot_id')
    status = models.IntegerField(verbose_name = "状态")
    price = models.FloatField(verbose_name = "价格")
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)



class ParkingLotSpace(models.Model):
    fk_parking_lot_id = models.ForeignKey(ParkingLot, db_column = 'fk_parking_lot_id', verbose_name = "停车场名称", editable = True)
    space_count = models.IntegerField(verbose_name = "车位数")
    fk_user_id = models.ForeignKey(User, db_column = 'fk_user_id', verbose_name = "相关用户")
    create_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '停车场车位'

    class Meta:
        verbose_name_plural = '停车场车位'



class ParkingRecord(models.Model):
    fk_user_id = models.ForeignKey(User, db_column = 'fk_user_id', verbose_name = "相关用户")
    latitude = models.FloatField(verbose_name = "纬度")
    longitude = models.FloatField(verbose_name = "经度")
    description = models.CharField(max_length = 50, verbose_name = "描述")
    pic = models.ImageField(upload_to = '.')
    parking_start_time = models.DateTimeField(verbose_name = "停车开始时间")
    parking_end_time = models.DateTimeField(verbose_name = "")
    create_time = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '用户停车记录'

    class Meta:
        verbose_name_plural = '用户停车记录'



class Offers(models.Model):
    fk_parking_lot_id = models.ForeignKey(ParkingLot, db_column = 'fk_parking_lot_id', verbose_name = "停车场名称")
    fk_user_id = models.ForeignKey(User, db_column = 'fk_user_id', verbose_name = "相关用户")
    detail = models.TextField(verbose_name = "优惠详情")
    start_time = models.DateTimeField(verbose_name = "开始时间")
    end_time = models.DateTimeField(verbose_name = "结束时间")
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.detail[:5]

    class Meta:
        verbose_name_plural = '优惠信息'



class UserLog(models.Model):
    fk_user_id = models.ForeignKey(User, db_column = 'fk_user_id', verbose_name = "相关用户")
    imei = models.CharField(max_length = 50)
    app_version = models.CharField(max_length = 20)
    create_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return '日志'

    class Meta:
        verbose_name_plural = '日志'


    type = models.IntegerField()
    fk_parking_lot_id = models.ForeignKey(ParkingLot, db_column = 'fk_parking_lot_id')
    imei = models.CharField(max_length = 50)
