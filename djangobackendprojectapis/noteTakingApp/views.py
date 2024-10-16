import json
from rest_framework import status
from rest_framework.decorators import api_view
from noteTakingApp.gram_check import check_grammer
from utils.Apiresponse import Api_Response

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