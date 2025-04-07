from django.shortcuts import render
from django.http import HttpResponse
from travel.models import Travel

# def travel_list(request, a_id):
#     travels = Travel.objects.get(id=a_id)
#     travels.views += 1
#     travels.save()  # 更新文章的浏览量
#     form = Travel()  # 初始化表单（假设直接使用模型）
#     context = {
#         'travel': travels,
#         'form': form
#     }
#     if request.method == 'POST':
#         form = travels(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return
#     travel_view = render(request, 'user/travel.html', context=context)
#     return HttpResponse(travel_view)
