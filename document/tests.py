from django.test import TestCase
from .models import DailyReport
from document.models import User
import random

class ReportTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Report.object.craete(
            dr_drafter = User.objects.get(pk=random.randint(1, 6)),
            dr_addressee = User.objects.get(user_name='안주영'),
            dr_status = '1',
            dr_title = 'TEST CASE에 의해 만들어진 객체'
        )
    
    def is_report_validate(self):
        rp = Report.objects.get(pk=1)
        f_l = rp._meta.get_field('dr_drafter').verbose_name
        self.assertEquals(f_l, '기안자')