from django.shortcuts import render


def home_list(request):
  return render(request, 'blog/home_list.html')
