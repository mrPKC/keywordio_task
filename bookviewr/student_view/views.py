from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Users, Books

# Create your views here.
def admin_signup(request):
    '''
        This method is to create a super user from the frontend.
        Params : 
            in request email, passwor is required
        response:
            html pages depending upon the status of the user
    '''
    email = request.POST.get("email",None)
    password = request.POST.get("password",None)

    if email == None or password == None:
        return render(request, "shop/admin_signup.html", {"check_empty_field":False})

    elif email != None and Users.objects.filter(email=email).exists():
        return render(request,"shop/admin_signup.html", {"error_message":True,"message":"User email already exist"})

    user = Users(email=email, password=password, is_staff=True, is_superuser=True)
    user.save()

    return render(request,"shop/admin_signup.html", {"success_message":True,"message":"Admin saved successfully"})

def student_view(request):
    '''
        This method is use to return the list of books available with pagination support
    '''
    book_list = Books.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 1)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'shop/book_list.html', { 'books': books })