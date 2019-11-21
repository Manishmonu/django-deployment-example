from django.shortcuts import render

# Create your views here.
# forwarded to the index page
def index(request):
	context_dict = {'text':'hello world',
					'number':100,
					}
	return render(request,"basic_app/index.html",context = context_dict)
# frowarded to the others page
def other(request):
	return render(request,"basic_app/other.html")
#forwarded to the template_url_relative page
def relative(request):
	return render(request,"basic_app/relative_url_templates.html")