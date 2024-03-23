import os
from django.conf import settings
from django.shortcuts import render
from .models import ImageCheck, InfoModel
from django.http import JsonResponse
from utils.image_check import check_handle
from web_system.settings import admin_title, index_info
import time


def index(request):
    context = {
        'title': admin_title,
        'index_info': index_info
    }

    return render(request, 'index.html', context=context)


def check(request):
    return render(request, 'check.html')


def upload_img(request):
    # 图片上传
    file = request.FILES.get('file')
    file_name = file.name
    file_name = '{}.{}'.format(int(time.time()), str(file_name).rsplit('.')[-1])
    with open(os.path.join(settings.MEDIA_ROOT, file_name), 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    upload_url = request.build_absolute_uri(settings.MEDIA_URL + file_name)
    ImageCheck.objects.create(file_name=file_name, file_url=upload_url)
    return JsonResponse({'code': 200, 'data': {'url': upload_url}})


def check_img(request):
    # 图片检测
    image_url = request.POST.get('img_url')
    if not image_url:
        return JsonResponse({'code': 400, 'message': '缺少必传的参数'})
    image_name = image_url.rsplit('/')[-1]
    image_path = os.path.join(settings.MEDIA_ROOT, image_name)
    pred_name = check_handle(image_path)

    obj = ImageCheck.objects.filter(file_name=image_name).last()
    obj.check_result = pred_name
    obj.save()
    # 查询是否有介绍信息
    flag = InfoModel.objects.filter(name=pred_name).first()
    if flag:
        info = flag.info
    else:
        info = '暂无介绍'

    return JsonResponse({'code': 200, 'data': {'pred_name': pred_name, 'info': info}})
