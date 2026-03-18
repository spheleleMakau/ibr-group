from django.shortcuts import render

# Data for companies
COMPANIES = [
	{"name": "Ekhaya African Cuisine", "icon": "🍽️", "description": "African food, spices, sauces, alcohol. Vision: Expand across Gauteng.", "link": "/companies/ekhaya/"},
	{"name": "IBR Foundation", "icon": "💙", "description": "Community programs, job seekers support, school gardening, youth development.", "link": "/foundation"},
	{"name": "IBR Agriculture", "icon": "🌱", "description": "South Africa & Botswana farms. Focus: vegetables + livestock.", "link": "/companies/agriculture/"},
	{"name": "IBR Mining & Engineering", "icon": "⛏️", "description": "Drilling, construction, geology. 200+ jobs created.", "link": "/companies/mining/"},
	{"name": "IBR Retail", "icon": "🛒", "description": "Retail operations across Africa.", "link": "/companies/retail/"},
	{"name": "White Eagle Investments", "icon": "🦅", "description": "Strategic investments for growth.", "link": "/companies/investments/"},
	{"name": "Crust Developments", "icon": "🏗️", "description": "Property and infrastructure development.", "link": "/companies/developments/"},
	{"name": "Tasty", "icon": "🍔", "description": "Quick service food brand.", "link": "/companies/tasty/"},
	{"name": "IBR Transport", "icon": "🚚", "description": "Logistics and transport solutions.", "link": "/companies/transport/"},
	{"name": "IBR Workshop", "icon": "🔧", "description": "Engineering and mechanical services.", "link": "/companies/workshop/"},
]

def home(request):
	return render(request, "core/home.html")

def about(request):
	return render(request, "core/about.html")

def companies(request):
	return render(request, "core/companies.html", {"companies": COMPANIES})

def foundation(request):
	return render(request, "core/foundation.html")

def contact(request):
	return render(request, "core/contact.html")
