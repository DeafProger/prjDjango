from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def index(request):
    output = f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>{request}</title>
</head>
<body>
    <div class="uk-container">
        <p>Explore our products and find what you're looking for.</p>
    </div>
</body>
</html>
    '''
    return HttpResponse(output)
