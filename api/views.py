from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PlanSerializers
from cms.models import Plan
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class PlanAPI(APIView):
    #permission_classes = (IsAuthenticated,)

    def get(self, request): # read
        plan_list = Plan.objects.filter(user=request.user)    
        serializer = PlanSerializers(plan_list,many=True) 
        return Response(serializer.data)
    
    def post(self,request): # create
        Plan.objects.create(
            user=request.user,
            title = request.POST.get('title'),
            date = request.POST.get('date')
        )
    #    print(request.POST)

        return Response({"is_success": True})

    def put(self, request): #update
        pass
    
    def delete(self,request): # delete
        pass

