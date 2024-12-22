from django.shortcuts import render

# Create your views here.

def login_view(request):
    # print(request.POST)
    # products = Product.objects.all()
    # response_text = ("my_products":products)
    from django.contrib.auth import authenticate
    from django.contrib.auth import login

    if request.method=='POST':
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(user=user, request=request)
        pass
    return render(request, "login.html")

