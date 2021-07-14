from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

from insServe.models import userData,content,comment,collection,like


# 登录/注册
def Login(request):
    # return HttpResponse(json.dumps({'ret':1,'msg':'登录成功'}))
    data = request.GET
    userMessage = eval(data['userdata'])
    print(userMessage)
    qs =content.objects.values()
    retList =list(qs)
    # print(userMessage['nickName'])
    try:
        #根据用户openid从数据库中查找用户数据
        userOpenid = userData.objects.get(openid=userMessage['openid'])
    except userData.DoesNotExist:
        record =userData.objects.create(nickName =userMessage['nickName'],
                                        gender=userMessage['gender'],
                                        city=userMessage['city'],
                                        province=userMessage['province'],
                                        avatarUrl=userMessage['avatarUrl'],
                                        openid=userMessage['openid']
        )
        return JsonResponse({'ret':0,'msg':'注册成功','retList':retList})

    return JsonResponse({'ret': 1, 'msg': '登录成功','retList':retList})





# 接收发布信息
def Release(request):
    data = json.loads(request.body)
    # print(data['contentImg'])
    # print(data['contentText'])
    # print(data['contentOpenid'])
    print(data['publisherProfile'])
    record = content.objects.create(contentImg=data['contentImg'],
                                    contentText=data['contentText'],
                                    contentPublisherOpenid=data['contentOpenid'],
                                    publisherProfile=data['publisherProfile'],
                                    publisherName=data['publisherName']
                                     )

    return JsonResponse({'ret':1,"msg":'发布成功'})


# 返回用户的个人动态
def ReturnPersonalInformation(request):
    data = request.GET
    print(data['openid'])
    personalInformation = content.objects.filter(contentPublisherOpenid=data['openid']).values()
    retlist = list(personalInformation)
    return JsonResponse({'ret':1,'retlist':retlist})



# 接收评论信息
def ReceiveComments(request):
    data = json.loads(request.body)
    # print(data['commentId'])
    record = comment.objects.create(commentId=data['commentId'],
                                    reviewerImage=data['reviewerImage'],
                                    reviewerName=data['reviewerName'],
                                    reviewerOpenid=data['reviewerOpenid'],
                                    reviewerContent=data['reviewerContent'])
    return JsonResponse({'ret':1,'msg':'发表评论成功！'})



# 根据该条信息的id获取该信息的评论信息
def SendComments(request):
    data = request.GET
    print(data['commentId'])
    comments =comment.objects.filter(commentId=data['commentId']).values()
    retlist =list(comments)
    return JsonResponse({'ret':1,'retlist':retlist})



# 添加收藏信息
def AddCollenction(request):
    data = request.GET
    print(data)
    record = collection.objects.create(DynamicId=data['DynamicId'],
                                       CollectorsOpenid=data['CollectorsOpenid']
                                       )
    return  JsonResponse({'rest':1,'msg':'收藏成功'})


# 删除收藏信息
def DelCollenction(request):
    data = request.GET
    print(data)
    delUserOpenid = data['delUserOpenid']
    try:
        collenctionMessage = collection.objects.get(CollectorsOpenid=delUserOpenid)
    except collection.DoesNotExist:
        return {
            'ret':1,
            'msg':'没有找到该条信息'
        }
    collenctionMessage.delete()
    return JsonResponse({'ret':1,'msg':'取消收藏成功'})


# 根据动态id拿详情的信息
def getDetail(request):
    data = request.GET
    print(data['contentId'])
    detailMessage = content.objects.filter(id=data['contentId']).values()
    print(detailMessage)
    retlist = list(detailMessage)
    print(retlist)
    return JsonResponse({'ret':1,'msg':'拿取detail数据成功','retlist':retlist})

# 添加一条点赞信息
# def addLikeMessage(request):
#     data = request.GET
#     print(data)
#     try:
#         likeMessage = like.objects.get(likeContentId=data['likeContentId'])
#     except like.DoesNotExist:
#         record = like.objects.create(likeContentId=data['likeContentId'],
#                                      likerOpenid=data['likerOpenid']
#                                      )
#     result = like.objects.get(likeContentId=data['likeContentId'])
#     result.likeCount += 1
#     return  JsonResponse({'rest':1,'msg':'点赞成功'})
