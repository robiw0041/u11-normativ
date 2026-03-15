from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login
from accounts.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.decorators import permission_required


def register_view(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")

    return render(request, "accounts/register.html", {"form": form})




def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.cleaned_data["user"]
            login(request, user)
            return redirect("post_list")  # asosiy sahifa

    return render(request, "accounts/login.html", {"form": form})


@login_required
def post_create(request):
    ...

@login_required
def post_update(request, pk):
    ...

@login_required
def post_delete(request, pk):
    ...


def post_list(request):
    ...

def post_detail(request, pk):
    ...

def logout_view(request):
    logout(request)
    return redirect("accounts:login")


from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            password=password
        )

        group = Group.objects.get(name='User')
        user.groups.add(group)

        return redirect('login')

    return render(request, 'accounts/register.html')

@permission_required('posts.add_post', raise_exception=True)
def post_create(request):
    ...


@permission_required('posts.change_post', raise_exception=True)
def post_update(request, id):
    ...

@permission_required('posts.delete_post', raise_exception=True)
def post_delete(request, id):
    ...