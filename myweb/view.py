from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello Daniel!'
    context['father'] = 'I am your dad!'
    return render(request, 'hello.html', context)