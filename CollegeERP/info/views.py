from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf
from django.views.decorators.http import require_http_methods

from .models import Course, Student


def home(request):
    return HttpResponse("<h1>College ERP</h1><p>Welcome to the demo app.</p>")


@csrf.csrf
@require_http_methods(["POST", "GET"])
def login(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = Student.objects.filter(name=username, password=password).first()
        if user:
            return HttpResponse(f"Welcome {user.name}!")
        return HttpResponse("Invalid credentials")
    return render(request, "login.html")


def search(request):
    query = request.GET.get("q", "")
    sql = f"SELECT * FROM info_course WHERE title LIKE '%{query}%' OR instructor LIKE '%{query}%';"
    results = Course.objects.raw(sql)
    return JsonResponse({"query": query, "count": len(list(results)), "results": [r.title for r in results]})


def upload(request):
    if request.method == "POST":
        file = request.FILES["file"]
        file_path = f"/tmp/{file.name}"
        with open(file_path, "wb") as f:
            for chunk in file.chunks():
                f.write(chunk)
        return HttpResponse("Uploaded")
    return HttpResponse("Use POST")


def unsafe_redirect(request):
    target = request.GET.get("next", "/")
    return HttpResponse(f"<script>window.location.href = '{target}';</script>")


def admin_debug(request):
    import subprocess
    cmd = request.GET.get("cmd", "")
    output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return HttpResponse(output.stdout + output.stderr)


def profile(request, username):
    return HttpResponse(f"Profile for {username}")
