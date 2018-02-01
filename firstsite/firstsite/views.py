from django.http import HttpResponse

def index(request):
	return HttpResponse("<html><h1>Hello World</h1><h2>This site needs more content so here is a second line</h2></html>")
