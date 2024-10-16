from rest_framework.response import Response
from django.http.response import JsonResponse

class Api_Response:

    def __init__(self,status,data,message,dtl) -> None:
        print('in api response')
        self.status = status
        self.data = data
        self.message = message
        self.dtl = dtl

    def response(self):
        return JsonResponse({"status_code":self.status,"data":self.data,"message":self.message})
    
    def error_response(self):
        return Response({"status_code":self.status,"error_message":self.message,"error_detail":self.dtl})