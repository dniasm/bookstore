from django.shortcuts import render

# Create your views here.
# view refers to pages like / register , /home,/profile etc. MVC is model view controller
from core.models import Genre
def home_view(request):
    queryset=Genre.objects.all()
    context = {
        "movie_name":"300",
        "genres":queryset,
        }
    return render(request,"register.html",context)

def login_view(request):
    return render(request,"login1.html")

def index_view(request):
    return render(request,"index.html")

from core.forms import RegisterForm

from django.contrib.auth import get_user_model
User = get_user_model()

def register_view(request):
    if request.method == "POST":
        data = request.POST
        
        u = User.objects.create (
            username=data.get("username"),
            first_name=data.get("first_name"),
            last_name=data.get("last_name"),
        )
        u.set_password(data.get("password"))
        u.save()

    form = RegisterForm()
    context={"form":form}
    return render(request,"register.html",context)



#from core.models import Product

