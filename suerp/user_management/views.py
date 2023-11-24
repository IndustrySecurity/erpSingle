from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from .forms import CustomUserForm

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_management/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # 重定向到用户列表
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'user_management/user_detail.html', {'form': form, 'user': user})
