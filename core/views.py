from django.shortcuts import render

# Data for companies
COMPANIES = [
    {"name": "Ekhaya African Cuisine", "icon": "🍽️", "description": "African food, spices, sauces, alcohol. Vision: Expand across Gauteng.", "link": "/companies/ekhaya/", "logo": "img/Ekhaya.png"},
    {"name": "IBR Foundation", "icon": "💙", "description": "Community programs, job seekers support, school gardening, youth development.", "link": "/foundation", "logo": "img/logo2.png"},
    {"name": "IBR Agriculture", "icon": "🌱", "description": "South Africa & Botswana farms. Focus: vegetables + livestock.", "link": "/companies/agriculture/", "logo": "img/agriculture.jpeg"},
    {"name": "IBR Mining & Engineering", "icon": "⛏️", "description": "Drilling, construction, geology. 200+ jobs created.", "link": "/companies/mining/", "logo": "img/mining.png"},
    {"name": "IBR Retail", "icon": "🛒", "description": "Retail operations across Africa.", "link": "/companies/retail/", "logo": "img/retail.jpeg"},
    {"name": "White Eagle Investments", "icon": "🦅", "description": "Strategic investments for growth.", "link": "/companies/investments/", "logo": "img/whiteeagle.jpeg"},
    {"name": "Crust Developments", "icon": "🏗️", "description": "Creative publishing company empowering young entrepreneurs through books, quotes, and educational content.", "link": "/companies/developments/", "logo": "img/crust.png"},
    {"name": "Tasty", "icon": "🍔", "description": "Quick service food brand.", "link": "/companies/tasty/", "logo": "img/Tasty.png"},
    {"name": "IBR Transport", "icon": "🚚", "description": "Logistics and transport solutions.", "link": "/companies/transport/", "logo": "img/transport.jpeg"},
    {"name": "IBR Workshop", "icon": "🔧", "description": "Engineering and mechanical services.", "link": "/companies/workshop/"},
]

def home(request):
	return render(request, "core/home.html", {"companies": COMPANIES} )

def about(request):
	return render(request, "core/about.html")

def companies(request):
	return render(request, "core/companies.html", {"companies": COMPANIES})

def contact(request):
	return render(request, "core/contact.html")

def agriculture(request):
	return render(request, "core/agriculture.html")

def mining(request):
	return render(request, "core/mining.html")

def retail(request):
	return render(request, "core/retail.html")

def investments(request):
	return render(request, "core/investments.html")

def developments(request):
	return render(request, "core/developments.html")

def foundation(request):
	return render(request, "core/foundation.html")
def tasty(request):
	return render(request, "core/tasty.html")

def transport(request):
	return render(request, "core/transport.html")

def workshop(request):
	return render(request, "core/workshop.html")

def ekhaya(request):
	return render(request, "core/ekhaya.html")

def ibr_africa(request):
	return render(request, "core/ibr_africa.html", {"companies": COMPANIES})

def ibr_foundation(request):
	return render(request, "core/ibr_foundation.html", {"companies": COMPANIES})

def ibr_holdings(request):
	return render(request, "core/ibr_holdings.html", {"companies": COMPANIES})