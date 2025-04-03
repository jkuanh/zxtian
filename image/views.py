from django.http import HttpResponse
from django.shortcuts import render
from .models import Image


def Images(request):
    """
    首页
    :param request:
    :return:
    """
    username = request.session.get("username", None)
    image = Image.objects.all()
    context = {
        'image': image,
        'title': '中香田'
    }
    if username:
        context["username"] = username
    response = render(request, 'upload_image.html', context=context)
    return response


def Image_list(request, a_id):
    images = Image.objects.get(id=a_id)
    images.views += 1
    images.save()  # 更新文章的浏览量
    form = Image()  # 初始化表单（假设直接使用模型）
    context = {
        'image': images,
        'form': form
    }
    if request.method == 'POST':
        form = images(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return
    image_view = render(request, 'user/image.html', context=context)
    return HttpResponse(image_view)
