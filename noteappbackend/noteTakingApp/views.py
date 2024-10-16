import json
import markdown
from rest_framework import status
from rest_framework.decorators import api_view
from noteTakingApp.gram_check import check_grammer
from django.contrib.auth.models import User
from utils.Apiresponse import Api_Response
from django.http.response import HttpResponse
from noteTakingApp.serializers import NoteSerializer
from noteTakingApp.models import Note


def __get_var(data,*args):
    out = []
    for x in args:
        out.append(data.get(x))
    return out




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
    

@api_view(['POST'])
def createNote(request):
    if request.method == 'POST':

        # TODO : change to get user_id from request ? cookie or header or param

        data = request.data 
        [title,description,user,markdown_txt] = __get_var(data,"title","desc","user","markdown_text")
        raw_html = None
        if markdown_txt:
            raw_html = markdown.markdown(markdown_txt)

        notsrlobj = NoteSerializer(data={
            "title":title,
            "description" : description,
            "user":user,
            "html_text" : raw_html 
        })

        if notsrlobj.is_valid():
            # print("no error in serializer")
            notsrlobj.save()
            return Api_Response(202,notsrlobj.data,"note added sucessfully","").response()
        else:
            print("error in serializer",notsrlobj.errors)
            return Api_Response(402,"","Error while adding note",notsrlobj.errors).error_response()

@api_view(['DELETE'])
def deleteNote(request,id):
    if request.method == 'DELETE':

        # TODO : change to get user_id from request ? cookie or header or param and validate request

        noteobj = Note.objects.filter(id=id).first()

        if noteobj:
            # print("no error in serializer")
            noteobj.delete()
            return Api_Response(202,noteobj.data,"note added sucessfully","").response()
        else:
            return Api_Response(402,"","Error while delete note",f"No Note found for id : {id}").error_response()


# @api_view(['GET'])
# def deleteNote(request,user_id):
#     if request.method == 'GET':

#         # TODO : change to get user_id from request ? cookie or header or param and validate request

#         noteobj = Note.objects.filter(user=user_id).all()

#         if noteobj:

#             notesrlobj = NoteSerializer(noteobj,many=True)
#             # print("no error in serializer")
#             noteobj.delete()
#             return Api_Response(202,notesrlobj.data,"note added sucessfully","").response()
#         else:
#             return Api_Response(402,"","Error while adding note",f"No Note found for user : {user_id}").error_response()


@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        data = request.data
        [username,email,password] = __get_var(data,"username","email","password")
        if username and password:
            try :
                usrobj = User.objects.create_user(username=username,email=email,password=password)

                if usrobj:
                    return Api_Response(200,"",'user created successfully','').response()
            except Exception as ex:
                return Api_Response(402,"","Error while registering user",str(ex)).error_response()


