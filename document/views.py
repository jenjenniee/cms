from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import View
from django.core import serializers
from .models import *
from django.contrib.auth.models import User
from datetime import date
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime,timedelta
from django.core.mail import EmailMessage


# Create your views here.
def main(request):

    user = request.user

    page = request.GET.get('page', 1)
    reports = DailyReport.objects.filter(Q(dr_drafter=user)|Q(dr_addressee=user)).order_by('-dr_created_at')
    reports, paginator_obj, _range = getPaginatorDatas(page, reports, 15)
    # paginator_obj= getPaginatorDatas(page, reports, 20)
    # _range = getPaginatorDatas(page, reports,)
    return render(request, 'document/document_main.html', {
        'reports' : reports,
        'p' : paginator_obj,
        'range' : _range
    })

class ReportRead(View):
    def get(self, request, *args, **kwargs):
        report = get_object_or_404(DailyReport, pk=kwargs.get('pk'))
        user = request.user
        # 읽을 수 있는가 확인
        if report.dr_drafter == user or report.dr_addressee == user:
            
            return render(request, 'document/dailyReport/read.html', {
                'report' : report,
            })

    # 결재 처리
    def post(self, request, *args, **kwargs):
        
        report = get_object_or_404(DailyReport, pk=kwargs.get('pk'))
        user = User.objects.all().order_by('-id')

        # 이미 처리가 되었다면 처리 불가
        if report.dr_status != '1':
            return JsonResponse({
                'msg' : '이미 결재 완료된 보고서입니다.',
            }, status=200)
        
        # 데이터 변경
        report.dr_status = request.POST.get('status')
        report.dr_feedback = request.POST.get('feedback')
        today = datetime.today() 
        report.dr_checked_at = today.strftime("%Y-%m-%d %H:%M:%S") 
        report.save(update_fields=['dr_status', 'dr_feedback', 'dr_checked_at'])

        if request.POST.get('feedback'): # 피드백있으면 유저 이메일로 발송 
            daily_content_list = DailyContent.objects.filter(dc_report=report)
            tommrow_will_list  = TommrowWill.objects.filter(tw_report=report)
            suggestion_list    = Suggestion.objects.filter(s_report=report)

            daily_content_msg = "금일보고\n"
            for number,daily_content in enumerate(daily_content_list):
                daily_content_msg += f"    {number+1}.{daily_content.dc_content}\n"

            tommrow_will_msg = "명일보고\n"
            for number, tommrow in enumerate(tommrow_will_list):
                tommrow_will_msg +=  f"    {number+1}.{tommrow.tw_content}\n"
            

            suggestion_msg = "건의사항\n"
            for number, suggestion in enumerate(suggestion_list):
                suggestion_msg += f"    {number+1}.{suggestion.s_content}\n"

            send_email = report.dr_drafter.user_email


            message = f"{request.POST.get('feedback')}\n"
            message += "================================\n"
            message += daily_content_msg
            message += tommrow_will_msg
            message += suggestion_msg
            
            #피드백 이메일 전송 
            email = EmailMessage(f'{report.dr_title} 피드백입니다.',message , to=[send_email,'2020011934@cju.ac.kr'])
            email.send()



        return JsonResponse({
            'msg' : '{0}의 보고서가 {1} 처리 되었습니다.'.format(report.dr_title, report.get_dr_status_display()),
        }, status=200)


class ReportWrite(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'document/dailyReport/write.html', {})

    def post(self, request, *args, **kwargs):
        
        dr_drafter = get_object_or_404(User, pk=request.user.id)
        rec = get_object_or_404(User, username = request.POST.get("reciever") )
        dr_addressee= get_object_or_404(User, pk=rec.id)

        if dr_drafter and dr_addressee:
            today = datetime.now() 
            report = DailyReport.objects.create(
                        user_id = request.user.id,
                        dr_drafter = dr_drafter,
                        dr_addressee = dr_addressee,
                        dr_created_at = today,
                        dr_status = '1',
                        dr_title = "{0} 일일보고_{1}".format(today.date(), dr_drafter.username)
                    )

            objects_mappings = {
                'dc' : DailyContent,
                'tw' : TommrowWill,
                's' : Suggestion
            }

            contents = [
                ('dc', request.POST.getlist('dc_content')),
                ('tw', request.POST.getlist('tw_content')),
                ('s', request.POST.getlist('s_content'))
            ]

            for c_list in contents:
                if c_list[1]:
                    for v in c_list[1]:
                        quries = createQueries(c_list[0], v, report, request)
                        objects_mappings[c_list[0]].objects.create(**quries)
            
        return redirect('document:document-main')

def createQueries(prefix, value, obj, request):
    q = {}
    if prefix == "dc" or prefix == "s":
        q['user_id'] = request.user.id
    q['{0}_{1}'.format(prefix, 'report')] = obj
    q['{0}_{1}'.format(prefix, 'content')] = value
    return q

def ajax_userlist(request): 
        context = {
            'users' : User.objects.all()
        }
        return render(request, 'document/list/userlist.html', context)

def getPaginatorDatas(page, queryset, count):
    if queryset is None:
        return 0

    try:
        _page = Paginator(queryset, count)
        _list = _page.page(page).object_list
        _paginator_obj = _page.page(page)
        index = _paginator_obj.number - 1
        max_index = len(_page.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index -3 else max_index
        _range = list(_page.page_range)[start_index:end_index]
        return _list, _paginator_obj, _range
    except Exception as e:
        pass
#        return getPaginatorDatas(1, queryset)
