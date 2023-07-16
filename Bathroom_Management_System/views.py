from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect, HttpResponse, reverse
from Bathroom_Management_System import models


# Create your views here.
# 主页
def home(request):
    return render(request, 'home.html')


# 登陆
def login(request):
    if request.method == 'POST':
        info_dic = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        user_obj = models.User.objects.filter(username=info_dic.get('username')).first()
        if user_obj:
            if info_dic['password'] == user_obj.password:
                return redirect(reverse('book_list'))
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户不存在')
    return render(request, 'login.html')


# 注册
def register(request):
    if request.method == 'POST':
        info_dic = {
            'username': request.POST.get('username'),
            'password': request.POST.get('password')
        }
        models.User.objects.create(**info_dic)
        return redirect(reverse('home'))
    return render(request, 'reg.html')


# 图书详情
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, 'book_list.html', locals())


# 添加图书
def add(request):
    all_author = models.Author.objects.all()
    all_publish = models.Publish.objects.all()
    if request.method == 'POST':
        info_dict = {
            'name': request.POST.get('name'),
            'price': float(request.POST.get('price')),
            'publish_id': int(request.POST.get('publish')),
            'publish_time': request.POST.get('publish_time'),
        }
        author_list = request.POST.getlist('author')
        book_obj = models.Book.objects.create(**info_dict)
        book_obj.author.add(*author_list)
        return redirect(reverse('book_list'))
    return render(request, 'add.html', locals())


# 修改图书信息
def edit(request, edit_id):
    edit_obj = models.Book.objects.filter(id=edit_id).first()
    all_author_obj = models.Author.objects.all()
    all_publish_obj = models.Publish.objects.all()
    if request.method == 'POST':
        info_dict = {
            'name': request.POST.get('name'),
            'price': float(request.POST.get('price')),
            'publish_id': int(request.POST.get('publish')),
            'publish_time': request.POST.get('publish_time'),
        }
        author_list = request.POST.getlist('author')
        models.Book.objects.filter(id=edit_id).update(**info_dict)
        edit_obj.author.set(author_list)
        return redirect(reverse('book_list'))
    return render(request, 'edit.html', locals())


# 删除图书信息
def del_book(request, del_id):
    models.Book.objects.filter(pk=del_id).delete()
    return redirect(reverse('book_list'))


# 作者信息
def author_info(request):
    all_author = models.Author.objects.all()
    return render(request, 'author_info.html', locals())


# 出版社信息
def publish_info(request):
    pass
