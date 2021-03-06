from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Hello World</h1>") #string of HTML code
	return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Contact</h1>")
	return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
	my_context = {
		"my_text"	: "This is about us",
		"my_number"	: 123,
		"my_list"	: [125, 353, 712, "qwe"]
	}
	return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
	#return HttpResponse("<h1>Social</h1>")
	return render(request, "social.html")