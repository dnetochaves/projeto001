from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    a = 10
    bb = 'teste jkdasfhasdkfhasdfhjkasdf'
    
    return render(request, 'recipes/index.html', {'a': 'a', 'teste': bb})