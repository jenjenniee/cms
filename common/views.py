from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.models import User


# def login(request):
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(request,username=username, password=raw_password)  # 사용자 인증
#             login(request, user)  # 로그인
#             return redirect('index')
#     else:
#         form = UserForm()
#     return render(request, 'common/.html', {'form': form})

#로그인
def login(request):
    context = {
        'msg' : '',
    }
    if request.method == "POST":
        user_objs = User.objects.filter(
                        user_id = request.POST.get('user_id'),
                        user_pw = request.POST.get('user_pw')
                    ).first()
        if user_objs:
            request.session['user_id']  = request.POST.get('user_id')
            request.session['user_pk']  = user_objs.pk
            request.session['user_name']= user_objs.user_name
            user_objs.save()
            return redirect("/")
        else:
            context['msg'] = 'LoginFail'
    return render(request,'commute/login')

    #로그아웃
def logout(request):
    if request.session.get('user_id') or request.session.get('user_name'):
        del request.session['user_id']
        del request.session['user_name']
        del request.session['user_pk']


    return redirect('/')