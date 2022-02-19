from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializer import BlogSerializer
from blog.models import Blog
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication




@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def api_view_detail(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog.author != user:
        return Response({'response': "You do not have permission"})

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)


@api_view(['PUT',])
@permission_classes((IsAuthenticated,))
def api_view_update(request,slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog.auther != user:
        return Response({'response': "You do not have permission"})

    if request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = "Blog Updated Successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
@permission_classes((IsAuthenticated,))
def api_view_delete(request, slug):
    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = request.user
    if blog.auther != user:
        return Response({'response': "You do not have permission"})

    if request.method == 'DELETE':
        operation = blog.delete()
        data = {}

        if operation:
            data['success'] = 'Successfully deleted blog'
        else:
            data['failure'] = 'Delete failed'

        return Response(data=data)

@api_view(['POST',])
def api_view_create(request):
    account = request.user
    blog = Blog(author=account)
    # blog = Blog()

    if request.method == 'POST':
        serializer = BlogSerializer(blog, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BlogApiListView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'desc', 'author__username')