# # from django.shortcuts import render, redirect
# # from .models import Project, Bug
# # from django.contrib.auth.models import User


# # def dashboard(request):
# #     projects = Project.objects.all()
# #     bugs = Bug.objects.all()
# #     return render(request, 'dashboard.html', {'projects': projects, 'bugs': bugs})


# # def add_project(request):

# #     if request.method == "POST":

# #         name = request.POST['name']
# #         description = request.POST['description']

# #         Project.objects.create(
# #             name=name,
# #             description=description,
# #             created_by=request.user   
# #         )

# #         return redirect('dashboard')

# #     return render(request, 'add_project.html')

# # def add_bug(request):

# #     projects = Project.objects.all()
# #     users = User.objects.all()

# #     if request.method == "POST":

# #         title = request.POST['title']
# #         description = request.POST['description']
# #         priority = request.POST['priority']
# #         status = request.POST['status']
# #         project_id = request.POST['project']
# #         assigned_id = request.POST['assigned_to']

# #         project = Project.objects.get(id=project_id)
# #         assigned_user = User.objects.get(id=assigned_id)

# #         Bug.objects.create(
# #             title=title,
# #             description=description,
# #             priority=priority,
# #             status=status,
# #             project=project,
# #             assigned_to=assigned_user
# #         )

# #         return redirect('dashboard')

# #     return render(request, 'add_bug.html', {
# #         'projects': projects,
# #         'users': users
# #     })


# from django.shortcuts import render, redirect
# from .models import Project, Bug
# from django.contrib.auth.models import User


# def dashboard(request):
#     projects = Project.objects.all()
#     bugs = Bug.objects.all()
#     return render(request, 'dashboard.html', {'projects': projects, 'bugs': bugs})


# def add_project(request):

#     if request.method == "POST":

#         name = request.POST['name']
#         description = request.POST['description']

#         Project.objects.create(
#             name=name,
#             description=description,
#             created_by=request.user   
#         )

#         return redirect('dashboard')

#     return render(request, 'add_project.html')

# def add_bug(request):

#     projects = Project.objects.all()
#     users = User.objects.all()

#     if request.method == "POST":

#         title = request.POST['title']
#         description = request.POST['description']
#         priority = request.POST['priority']
#         status = request.POST['status']
#         project_id = request.POST['project']
#         assigned_id = request.POST['assigned_to']

#         project = Project.objects.get(id=project_id)
#         assigned_user = User.objects.get(id=assigned_id)

#         Bug.objects.create(
#             title=title,
#             description=description,
#             priority=priority,
#             status=status,
#             project=project,
#             assigned_to=assigned_user
#         )

#         return redirect('dashboard')

#     return render(request, 'add_bug.html', {
#         'projects': projects,
#         'users': users
#     })


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from .models import Project, Bug

def home(request):
    return render(request, 'home.html')

# def signup_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         if User.objects.filter(username=username).exists():
#             return render(request, 'signup.html', {'error': 'Username already exists'})
#         user = User.objects.create_user(username=username, password=password)
#         login(request, user)
#         return redirect('dashboard')
#     return render(request, 'signup.html')

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('dashboard')
#         return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')
def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')  # changed here
        password = request.POST.get('password')  # changed here

        if not username or not password:
            return render(request, 'signup.html', {'error': 'Please enter both username and password'})

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')  # changed here
        password = request.POST.get('password')  # changed here

        if not username or not password:
            return render(request, 'login.html', {'error': 'Please enter both username and password'})

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    projects = Project.objects.all()
    bugs = Bug.objects.all()
    return render(request, 'dashboard.html', {'projects': projects, 'bugs': bugs})

@login_required(login_url='login')
def add_project(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        Project.objects.create(name=name, description=description, created_by=request.user)
        return redirect('dashboard')
    return render(request, 'add_project.html')

@login_required(login_url='login')
def add_bug(request):
    projects = Project.objects.all()
    users = User.objects.all()
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        priority = request.POST['priority']
        status = request.POST['status']
        project_id = request.POST['project']
        assigned_id = request.POST['assigned_to']
        project = Project.objects.get(id=project_id)
        assigned_user = User.objects.get(id=assigned_id)
        Bug.objects.create(title=title, description=description, priority=priority, status=status, project=project, assigned_to=assigned_user)
        return redirect('dashboard')
    return render(request, 'add_bug.html', {'projects': projects, 'users': users})
    
# ---------------- Project Update ----------------
@login_required(login_url='login')
def update_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.name = request.POST['name']
        project.description = request.POST['description']
        project.save()
        return redirect('dashboard')
    return render(request, 'update_project.html', {'project': project})

# ---------------- Project Delete ----------------
@login_required(login_url='login')
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == "POST":
        project.delete()
        return redirect('dashboard')
    return render(request, 'delete_project.html', {'project': project})

# ---------------- Bug Update ----------------
@login_required(login_url='login')
def update_bug(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    projects = Project.objects.all()
    users = User.objects.all()
    if request.method == "POST":
        bug.title = request.POST['title']
        bug.description = request.POST['description']
        bug.priority = request.POST['priority']
        bug.status = request.POST['status']
        bug.project = Project.objects.get(id=request.POST['project'])
        bug.assigned_to = User.objects.get(id=request.POST['assigned_to'])
        bug.save()
        return redirect('dashboard')
    return render(request, 'update_bug.html', {'bug': bug, 'projects': projects, 'users': users})

# ---------------- Bug Delete ----------------
@login_required(login_url='login')
def delete_bug(request, bug_id):
    bug = get_object_or_404(Bug, id=bug_id)
    if request.method == "POST":
        bug.delete()
        return redirect('dashboard')
    return render(request, 'delete_bug.html', {'bug': bug})