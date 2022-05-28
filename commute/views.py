from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.http import HttpResponse
from .utils import get_client_ip
from datetime import datetime,timedelta,date
from .models import Commute
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#로그인 해야 접근 가능
# @login_required
def commute_home(request):
    import calendar

    start_date = request.GET.get('start')
    end_date   = request.GET.get('end')
    
    if start_date and end_date: # client 받은 시작날짜와 종료날짜가 있으면
        commutes = Commute.objects.filter(commute_date__date__gte=start_date,commute_date__date__lte=end_date).order_by('-id')
    else:
        commutes = Commute.objects.all().order_by('-id')
    
    users = User.objects.all().order_by('-id')
    

    if request.GET.get('year') and request.GET.get('month'):

        cur_datetime = datetime(int(request.GET.get('year')),int(request.GET.get('month')),1)
        
    else:
        cur_datetime = datetime.now()
    

    user_commute_conditions = {}
    
    for user in users:
        commute_status_list = []
        for day in range(calendar.monthrange(cur_datetime.year,cur_datetime.month)[1]):
            day = day + 1
            compare_date = datetime(cur_datetime.year,cur_datetime.month,day)
            if compare_date.date() < datetime.now().date():
                commute_status_list.append(False)
            else:
                commute_status_list.append(None)

        user_commute_conditions.update({
            user.user_name:{
                'commute_status': commute_status_list, # 1일 ~ 31일까지 출퇴근 여부 초기값으로 None
                'include_weekends_commute_rate': None, #주말포함 출근율
                'include_weekends_number_absences': None, #주말포함 결근 일수
                'exclude_weekends_commute_rate': None,
                'exclude_weekends_number_absences': None
            }
        })
    

    #cur_datetime = datetime.now()

    commute_conditions = Commute.objects.filter(commute_date__year=cur_datetime.year,commute_date__month=cur_datetime.month).order_by('commute_date')
    
    for c in commute_conditions:
        username = c.user.username
        day = c.commute_date.day
        
        if c.commute_category == '1' or c.commute_category == '3':
            user_commute_conditions[username]['commute_status'][day-1] = True
        

    for key in user_commute_conditions: 
        #주말 포함 출근율과 결근일수 
        true_cnt = user_commute_conditions[key]['commute_status'].count(True)
        false_cnt = user_commute_conditions[key]['commute_status'].count(False)
        try:
            user_commute_conditions[key]['include_weekends_commute_rate'] = f'{int(true_cnt / (true_cnt+false_cnt) * 100)}%'
        except ZeroDivisionError:
            user_commute_conditions[key]['include_weekends_commute_rate'] = '0%'

        user_commute_conditions[key]['include_weekends_number_absences'] = false_cnt

        exclude_weekends_true_cnt = 0 # 주말제외 true 개수
        exclude_weekends_false_cnt = 0 # 주말제외 false 개수
        #주말 제외 출근율과 결근일수 구하기
        for i,value in enumerate(user_commute_conditions[key]['commute_status']):
            weekday = date(cur_datetime.year,cur_datetime.month,i+1).weekday()

            # None 또는 토요일 또는 일요일 제외
            if value is None or weekday == 5 or weekday == 6: continue 
            
            if value:
                exclude_weekends_true_cnt += 1
            else:
                exclude_weekends_false_cnt += 1
        try:
            user_commute_conditions[key]['exclude_weekends_commute_rate'] = f'{int(exclude_weekends_true_cnt / (exclude_weekends_true_cnt+exclude_weekends_false_cnt) * 100)}%'
        except ZeroDivisionError:
            user_commute_conditions[key]['exclude_weekends_commute_rate'] = '0%'
        user_commute_conditions[key]['exclude_weekends_number_absences'] = exclude_weekends_false_cnt


    weekdays = ['월','화','수','목','금','토','일']
    
    day_list = [] #[1일(월),2일(화)....]
    for day in range(calendar.monthrange(cur_datetime.year,cur_datetime.month)[1]):
        weekday = date(cur_datetime.year,cur_datetime.month,day+1).weekday()
        day_list.append(f'{day+1}일({weekdays[weekday]})')

    context = {
        'length': len(commutes),
        'commutes': commutes,
        'start': start_date,
        'end': end_date,
        'user_commute_conditions': user_commute_conditions,
        'day_list': day_list,
        'month': cur_datetime.month,
        'year': cur_datetime.year
    }

    
    return render(request,'commute/commute_home.html',context)