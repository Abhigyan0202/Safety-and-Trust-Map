from django.shortcuts import render

def test_tailwind(request):
    return render(request, "app/test_tailwind.html")