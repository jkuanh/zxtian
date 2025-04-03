
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Article
from django.core.mail import send_mail
from django.conf import settings
from home.models import User
import random
import hashlib


# def index(request):
#     """
#     首页
#     :return:
#     """
#     # 需要在这里进行判断是否已经登录
#     # cookie 是客户端存储数据的一种机制，但是由服务端来设置
#     # 一旦设置完之后，下次这个浏览器再次请求这个网站的时候会把我们设置的cookie提交过来
#     # session_id = request.COOKIES["sessionid"]
#     #
#     # filename = session_id + ".txt"
#     # file_path = os.path.join(settings.BASE_DIR, "session", filename)
#     # with open(file_path, "r", encoding="utf-8") as fp:
#     #     content = fp.read()
#     #
#     # username = json.loads(content)["username"]
#     # 防止将session删除之后出现语法错误，所以使用get方式来获取值
#     username = request.session.get("username", None)
#
#     articles = Article.objects.all()  # 获取所有的文章数据
#     context = {
#         "articles": articles,
#         "title": "小淘宝博客网"
#     }
#
#     if username:
#         context["username"] = username
#     response = render(request, "index.html", context=context)
#     return response
#
#
# def detail(request, a_id):
#     print(a_id)
#     article = Article.objects.get(id=a_id)
#     context = {
#         "article": article
#     }
#     return render(request, "detail.html", context=context)
#
#
# def register(request):
#     """
#     用户注册
#     :param request:
#     :return:
#     """
#     method = request.method  # 获取请求的方法
#     if method == "GET":
#         return render(request, "register.html")
#     else:
#         # 获取提交的数据
#         username = request.POST["username"]  # 获取用户名
#         password = request.POST["password"]  # 获取密码
#         c_password = request.POST["c_password"]  # 获取确认密码
#         email = request.POST["email"]  # 获取邮箱
#         email_code = request.POST["email_code"]  # 获取邮箱验证码
#
#         """
#         验证邮箱验证码是否正确
#         """
#         code = request.session.get("email_code", None)  # 从session中获取邮箱验证码
#         if email_code != code:
#             message = "邮箱验证错误，请输入正确的验证码"
#             context = {
#                 "message": message,
#                 "return_url": "/register",
#                 "return": "返回到注册页面"
#             }
#             return render(request, "error.html", context=context)
#
#         """
#         验证用户名
#         """
#         try:
#             user = User.objectes.get(username=username)
#             message = "用户名称已经存在，请更换用户名"
#             context = {
#                 "message": message,
#                 "return_url": "/register",
#                 "return": "返回到注册页面"
#             }
#             return render(request, "error.html", context=context)
#
#         except Exception:
#             pass
#
#         """
#         确认密码和确认密码是否相等
#         """
#
#         """
#         将用户提交的数据存储到数据库里面
#         """
#         # 密码使用md5加密
#         cipher_text = hashlib.md5(password.encode("utf-8")).hexdigest()
#         User.objects.create(
#             username=username,
#             email=email,
#             password=cipher_text
#         )
#
#         message = "恭喜你，注册成功!"
#         context = {
#             "message": message,
#             "return_url": "/login",
#             "return": "跳转到登录界面"
#         }
#
#         return render(request, "success.html", context=context)
#
#
# def login(request):
#     """
#     登录界面
#     :param request:
#     :return:
#     """
#
#     method = request.method  # 获取请求的方法
#     if method == "GET":
#         return render(request, "login.html")
#     else:
#         username = request.POST["username"]  # 获取用户名
#         password = request.POST["password"]  # 获取密码
#
#         # 判断用户名是否已经存在
#         try:
#             user = User.objects.get(username=username)
#
#             # 判断密码是否正确
#             cipher_text = hashlib.md5(password.encode("utf-8")).hexdigest()
#             if cipher_text == user.password:
#                 """
#                         1、生成一个唯一的字符串
#                         2、我把这个唯一的字符串写入cookie中
#                         3、用这个唯一的字符串来在服务端创建一个文件
#                         4、把用户信息存入文件中
#                 """
#                 import time
#
#                 # timestamp = str(time.time())  # 用时间戳来进行加密
#                 # session_id = hashlib.md5(timestamp.encode("utf-8")).hexdigest()
#                 # filename = session_id + ".txt"
#                 # file_path = os.path.join(settings.BASE_DIR, "session", filename)
#                 # with open(file_path, "w", encoding="utf-8") as fp:
#                 #     info = json.dumps({"username": username})
#                 #     fp.write(info)
#
#                 message = "登录成功!"
#                 context = {
#                     "message": message,
#                     "return_url": "/",
#                     "return": "跳转到首页"
#                 }
#                 response = render(request, "success.html", context=context)
#                 # response.set_cookie("sessionid", session_id)
#                 request.session["username"] = username
#                 return response
#
#             else:
#                 message = "密码错误，请重新输入!"
#                 context = {
#                     "message": message,
#                     "return_url": "/login",
#                     "return": "返回到登录界面"
#                 }
#
#                 return render(request, "error.html", context=context)
#
#
#
#
#         except Exception as e:
#             message = "用户名不存在!"
#             context = {
#                 "message": message,
#                 "return_url": "/login",
#                 "return": "返回到登录界面"
#             }
#
#             return render(request, "error.html", context=context)
#
#
# def logout(request):
#     """
#     退出
#     :param request:
#     :return:
#     """
#
#     del request.session["username"]
#     # 重定向到登录界面
#     return HttpResponseRedirect("/")
#
#
# def send_verification_code(request):
#     """
#     发送邮件
#     :return:
#     """
#
#     email = request.POST["email"]
#     # 生成一个6位数的验证码
#     ver_code = gen_ver_code(6)
#     request.session["email_code"] = ver_code  # 将邮箱验证码存储到session中
#
#     # 发送邮件
#     send_mail(
#         subject="[小小淘宝]邮箱验证码",
#         message=f"您的验证码是：{ver_code}",
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         recipient_list=[email]
#     )
#
#     return JsonResponse({"success": 1, "msg": "发送成功"})
#
#
# def gen_ver_code(nums):
#     """
#     生成指定个数验证码
#     :param nums:
#     :return:
#     """
#     string = "234g4jak56k5h3g3aomadmfaiwqrr87363asmasejrjqrr247534939mwrweurk35674h"
#     max_index = len(string) - 1
#
#     random_str = ""
#     for x in range(nums):
#         i = random.randint(0, max_index)
#         char = string[i]
#         random_str += char
#
#     return random_str
#
#
# def user_center(request):
#     """
#     用户中心
#     :return:
#     """
#     # 判断是否已经登录
#     username = request.session.get("username", None)
#     if not username:
#         # 用户没有登录
#         return HttpResponseRedirect("/login")  # 重定向到登录界面
#
#     articles = Article.objects.filter(author=username)
#     return render(request, "user_center.html", {"articles": articles})
#
#
# def submit_article(request):
#     """
#     文章发布
#     """
#     # 获取数据
#     title = request.POST["title"]  # 获取标题
#     description = request.POST["description"]  # 获取摘要
#     content = request.POST["content"]  # 获取内容
#
#     # 作者
#     author = request.session["username"]
#
#     article = Article.objects.create(
#         title=title,
#         description=description,
#         content=content,
#         author=author
#     )
#
#     return JsonResponse({"code": 0, "msg": "添加成功!", "a_id": article.id})
