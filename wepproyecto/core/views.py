from django.shortcuts import render, HttpResponse

htmlBase="""
    <h1>Mi proyecto Web</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/store/">Tienda</a></li>
        <li><a href="/contact/">Contacto</a></li>
        <li><a href="/portfolio/">Portafolio</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")
def about(request):
    return render(request, "core/about.html")
def store(request):
    return render(request, "core/store.html")
def contact(request):
    return render(request, "core/contact.html")
def portfolio(request):
    return render(request, "core/portfolio.html")
