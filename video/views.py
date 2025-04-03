from django.shortcuts import render
from .models import Video
from django.http import HttpResponse


def Videos(request, a_id):
    video = Video.objects.get(id=a_id)
    # video.views += 1
    video.save()  # 更新文章的浏览量
    form = Video()  # 初始化表单（假设直接使用模型）
    context = {
        'video': video,
        'form': form
    }
    if request.method == 'POST':
        form = video(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return
    video_view = render(request, 'video/video.html', context=context)
    return HttpResponse(video_view)
