import json
import markdown
from rest_framework import status
from rest_framework.decorators import api_view
from noteTakingApp.gram_check import check_grammer
from utils.Apiresponse import Api_Response
from django.http.response import HttpResponse

@api_view(['GET', 'POST'])
def checkNoteGrammer(request):

    # if request.method == 'GET':
    #     return Response({"pass":"pass"})

    if request.method == 'POST':
        body = request.data
        # print(body)
        note = body.get('note')
        if check_grammer(note):
            return Api_Response(status=200,data="note is grammetically correct",message="Success",dtl="").response()
        else:
            return Api_Response(status=400,data="note is not grammetically correct",message="Success",dtl="").response()
        # return Response({"fail":"pass"})
    else:
        return Api_Response(status=450,data="",message="Wrong Request Type",dtl="").error_response()
    
@api_view(['POST'])
def renderMDtoHTML(request):
    if request.method == 'POST':
        data = request.data
        print('data------------',type(data))
        # json_Data = json.dumps(data)
        md_txt = data.get('markdown_text')
        if md_txt:
            rawhtml = markdown.markdown(md_txt)
            return HttpResponse(rawhtml)
    else:
        return Api_Response(status=450,data="",message="Wrong Request Type",dtl="").error_response()
    