from django.db import models


# 用户信息表
class userData(models.Model):
    #用户名称
    nickName= models.CharField(max_length=100)
    #用户性别
    gender = models.IntegerField()
    #用户城市
    city = models.CharField(max_length=100)
    #用户省份
    province = models.CharField(max_length=100)
    #用户头像地址
    avatarUrl = models.CharField(max_length=10000)
    #用户的openid
    openid = models.CharField(max_length=10000)


# 用户发布的内容表
class content(models.Model):
    #内容图片
    contentImg = models.CharField(max_length=100000,blank=True)
    #内容文本
    contentText = models.CharField(max_length=10000,blank=True)
    #内容发布者openid
    contentPublisherOpenid = models.CharField(max_length=100000,blank=True)
    #发布者名称
    publisherName = models.CharField(max_length=100,blank=True)
    #发布者头像
    publisherProfile = models.CharField(max_length=100000,blank=True)

# 接收评论表
class comment(models.Model):
    #评论者头像
    reviewerImage = models.CharField(max_length=10000)
    #评论者的openid
    reviewerOpenid = models.CharField(max_length=10000)
    #评论内容
    reviewerContent = models.CharField(max_length=10000)
    #评论者名称
    reviewerName = models.CharField(max_length=10000)
    #该条评论的id
    commentId = models.CharField(max_length=100000)


#收藏表
class collection(models.Model):
    #被收藏动态的id
    DynamicId = models.CharField(max_length=10000)
    #收藏该动态用户的openid
    CollectorsOpenid = models.CharField(max_length=10000)


# 用户点赞表
class like(models.Model):
    # 被点赞的动态的id
    likeContentId = models.CharField(max_length=10000)
    # 点赞者openid
    likerOpenid = models.CharField(max_length=100000)
    #点赞的数量
    likeCount = models.IntegerField(default=0)

##python manage.py migrate

##python manage.py makemigrations