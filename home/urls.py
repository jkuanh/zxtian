from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import (index, detail, travels, search, test2, Images, Image,
                        register, send_verification_code, login, user_center, logout, submit_article)

urlpatterns = [
    path('', index),
    path("detail/<int:a_id>", detail),
    path('wangeditor/', include('wangeditor.urls')),
    path('register', register),
    path('index/', index),
    path("send_verification_code", send_verification_code),
    path("login", login),
    path('logout', logout),
    path("user_center", user_center),
    path("submit_article", submit_article),
    path('travel/<int:a_id>', travels),
    # path('Images/<int:a_id>', Images),
    path('test2/', test2),
    path('search/', search),
    path('upload_image/', Images),
    path('Image_list/<int:a_id>', Image),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
