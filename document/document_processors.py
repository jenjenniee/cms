from document.models import User
from document.models import DailyReport
from django.db import connection 
from django.db.models import Q

def sessionUserProcessor(request):
    if request.session.get('user_pk'):
        user = User.objects.get(pk=request.session['user_pk'])
        report = DailyReport.objects.filter(Q(dr_drafter=user)|Q(dr_addressee=user)).filter(dr_status='1')

        return {
            's_user' : user,
            'report_cnt' : len(report)
        }
    return {'s_user' : None }
