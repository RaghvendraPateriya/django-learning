from django.http import HttpResponse
from django.views.generic import View

def my_view(request):
    # print(request)
    username = request.GET.get('username')
    if username:
        return HttpResponse(f"Hello World !! {username}")
    return HttpResponse(f"Hello World !!")


def view_named_query_sting(request, username):
    return HttpResponse(f"Hello {username}")


# Class Based View - Generic
class MyView(View):

    def get(self, request):
        return HttpResponse("Hello my first class based view!!!")

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass