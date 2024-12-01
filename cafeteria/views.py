from django.shortcuts import render
from .models import Menu

def home(request):
    menu_items = Menu.objects.all()  # 从数据库中获取菜单数据
    return render(request, 'home.html', {'menu_items': menu_items})


