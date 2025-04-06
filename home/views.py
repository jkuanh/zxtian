import hashlib
import random
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from article.models import Article, Image, Travel, Video, User
import os


def index(request):
    """
    首页
    :return:
    """
    # 防止将session删除之后出现语法错误，所以使用get方式来获取值
    username = request.session.get("username", None)
    articles = Article.objects.all()  # 获取所有的文章数据
    image = Image.objects.all()  # 获取最新图片
    travel = Travel.objects.all()
    video = Video.objects.all()
    context = {
        'articles': articles,
        'image': image,
        'travels': travel,
        'video': video,
        'title': '中香田'
    }
    if username:
        context["username"] = username
    response = render(request, 'user/index.html', context=context)
    return response


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


def traveled(request):
    """
    首页
    :param request:
    :return:
    """
    username = request.session.get("username", None)
    traver = Travel.objects.all()
    context = {
        'travel': traver,
        'title': '中香田'
    }
    if username:
        context["username"] = username
    response = render(request, 'travel_image.html', context=context)
    print(response)
    return response


def detail(request, a_id):
    article = Article.objects.get(id=a_id)
    article.views += 1
    article.save()  # 更新文章的浏览量
    context = {
        'article': article
    }
    return render(request, 'user/detail.html', context=context)


def travels(request, a_id):
    travel = Travel.objects.get(id=a_id)
    travel.views += 1
    travel.save()  # 更新文章的浏览量
    form = Travel()  # 初始化表单（假设直接使用模型）
    context = {
        'travel': travel,
        'form': form
    }
    if request.method == 'POST':
        form = travel(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return
    travel_view = render(request, 'user/travel.html', context=context)
    return HttpResponse(travel_view)


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


def register(request):
    """
    用户注册
    :return:
    """
    method = request.method  # 获取请求的方法
    if method == "GET":
        return render(request, 'user/register.html')
    else:
        # 获取提交的数据
        username = request.POST["username"]  # 获取用户名
        password = request.POST["password"]  # 获取密码
        c_password = request.POST["c_password"]  # 获取确认密码
        email = request.POST["email"]  # 获取邮箱
        email_code = request.POST["email_code"]  # 获取邮箱验证码
        """
        验证邮箱验证码是否正确
        """
        code = request.session.get('email_code', None)  # 从session中获取邮箱验证码
        if email_code != code:
            message = "邮箱验证错误, 请输入正确的验证码"
            context = {
                "message": message,
                "return_url": "/register",
                "return": "返回到注册页面"
            }
            return render(request, 'user/error.html', context=context)

        """
        验证用户名
        """
        try:
            user = User.odjectes.get(username=username)
            message = "用户名称已经存在，请更换用户名"
            context = {
                "message": message,
                "return_url": "/register",
                "return": "返回到注册页面"
            }
            return render(request, 'user/error.html', context=context)

        except Exception:
            pass

        """
        确认密码和确认密码是否相等
        """

        """
        将用户提交的数据存储到数据库里面
        """
        # 密码使用md5加密
        cipher_text = hashlib.md5(password.encode("utf-8")).hexdigest()
        User.objects.create(
            username=username,
            email=email,
            password=cipher_text
        )
        message = "恭喜您, 注册成功!"
        context = {
            'message': message,
            'return_url': "/login",
            "return": "跳转到登录界面"
        }

        return render(request, "user/login.html", context=context)


def login(request):
    """
    登录界面
    :param request:
    :return:
    """
    method = request.method  # 获取请求的方法
    if method == "GET":
        return render(request, "user/login.html")
    else:
        username = request.POST["username"]  # 获取用户名
        password = request.POST["password"]  # 获取密码
        # 判断用户名是否已经存在
        try:
            user = User.objects.get(username=username)
            # 判断密码是否正确
            cipher_text = hashlib.md5(password.encode("utf-8")).hexdigest()
            if cipher_text == user.password:
                """
                   1、生成一个唯一的字符串
                   2、我把这个唯一的字符串写入cookie中
                   3、用这个唯一的字符串来在服务端创建一个文件
                   4、把用户信息存入文件中
                """
                import time
                message = "登录成功!"
                context = {
                    "message": message,
                    "return_url": "/",
                    "return": "跳转到首页"
                }
                response = render(request, "user/success.html", context=context)
                request.session["username"] = username
                return response
            else:
                message = "密码错误, 请重新输入!"
                context = {
                    "message": message,
                    "return_url": "/login",
                    "return": "返回到登录界面"
                }
                return render(request, "user/error.html", context=context)

        except Exception as e:
            message = "用户名不存在!"
            context = {
                'message': message,
                'return_url': "/login",
                'return': "返回到登录界面"
            }

            return render(request, "user/error.html", context=context)


def logout(request):
    """
    退出
    :param request:
    :return:
    """

    del request.session["username"]
    # 重定向到登录界面
    return HttpResponseRedirect("/")


def send_verification_code(request):
    """
    发送邮件
    :return:
    """
    email = request.POST["email"]
    # 生成6位验证码
    ver_code = gen_ver_code(6)
    request.session["email_code"] = ver_code  # 将邮箱验证码存储到session中
    # 发送邮件
    send_mail(
        subject='[博客网]邮箱验证码',
        message=f'您的验证码是: {ver_code}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email]
    )
    return JsonResponse({'success': 1, 'msg': '发送成功'})


def gen_ver_code(nums):
    """
    生成指定个位数验证码
    :param nums:
    :return:
    """
    string = '0123456789qazxswedcvfrtgbnhyujmkilopLJLKGHAIFHJKV'
    max_index = len(string) - 1
    random_str = ""
    for x in range(nums):
        s = random.randint(0, max_index)
        char = string[s]
        random_str += char

    return random_str


def user_center(request):
    """
    用户中心
    :return:
    """
    # 判断是否已经登录
    username = request.session.get("username", None)
    if not username:
        # 用户没有登录
        return HttpResponseRedirect("/login")  # 重定向到登录界面

    articles = Article.objects.filter(author=username)
    article_count = len(articles)  # 文章总数
    total_views = 0
    for article in articles:
        total_views += article.views
    return render(request, "user/user_center.html",
                  {"articles": articles, "article_count": article_count, "total_views": total_views})


def submit_article(request):
    """
    文章发布
    """
    # 获取数据
    title = request.POST["title"]  # 获取标题
    description = request.POST["description"]  # 获取摘要
    content = request.POST["content"]  # 获取内容
    # 作者
    author = request.session["username"]

    article = Article.objects.create(
        title=title,
        description=description,
        content=content,
        author=author
    )

    return JsonResponse({"code": 0, "msg": "添加成功!", "a_id": article.id})


def test(request):
    """
    测试函数
    :param request:
    :return:
    """
    print("请求头:", request.headers, type(request.headers))
    print("是否是Ajax请请求:", request.is_ajax())
    print("使用的请求方法是:", request.method)
    print("请求路径:", request.path)
    print("请求协议:", request.scheme)

    method = request.methhod
    if method == "GET":
        html = """
            <form  method="post">
                <input type="text" name="username" placeholder="请输入你的用户名" /><br/>
                <input type="password" name="password" placeholder="请输入你的密码" /><br/>
                <button type="submit">提交</button>

            </form>
        """
    else:
        print(request.POST)
        username = request.POST["username"]  # 获取用户
        password = request.POST["password"]  # 获取密码
        print(username, password)

    return HttpResponse(html)


def test2(request):
    """
    文件上传
    :param request:
    :return:
    """

    method = request.method
    if method == "GET":
        html = """
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="image" /><br/><br/>
            <button type="submit">上传文件</button>
        </form>
        """

        return HttpResponse(html)
    else:
        image = request.FILES.get("image", None)
        if image:
            # 1、获取文件的名称
            file_name = image.name
            file_path = os.path.join(settings.BASE_DIR, "static", "uploads", file_name)
            # 打开文件
            with open(file_path, "wb")as fp:
                for chunk in image.chunks():
                    fp.write(chunk)

    return HttpResponse("上传成功")


def test3(request):
    """
    响应：
    1、响应一个html文档(html字符串)
    2、响应一个JSON字符串(通常用于接口请求)
    3、重定向,告诉浏览器去请求一个新的地址(用来做跳转)
    """
    return HttpResponseRedirect("https://www.baidu.com")


def search(request):
    """
    文章搜索
    :param request:
    :return:
    """
    key_word = request.GET["q"]
    articles = Article.objects.filter(title__icontains=key_word).order_by("-views")
    travel = Travel.objects.filter(title__icontains=key_word).order_by("-views")
    context = {
        "articles": articles,
        'travel': travel,
        "key_word": key_word
    }
    return render(request, 'user/search.html', context=context)
