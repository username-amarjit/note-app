from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET', 'POST'])
def createBlog(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # snippets = Snippet.objects.all()
        # serializer = SnippetSerializer(snippets, many=True)
        return Response({"pass":"pass"})

    elif request.method == 'POST':
        # serializer = SnippetSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"fail":"pass"})
