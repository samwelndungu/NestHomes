from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'properties/index.html')

def property_list(request):
    properties = Property.objects.filter(is_available=True)
    query = request.GET.get('q', '')
    if query:
        properties = properties.filter(
            Q(title__icontains=query) | Q(location__icontains=query) | Q(price__icontains=query) 
        )
    
    return render(request, 'properties/properties.html', {'properties': properties})

def buy_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        property.is_available = False
        property.save()
        return redirect('property_list')

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {'property': property})
# This view handles the property detail page, fetching the property by primary key (pk)
def contact_view(request):
    return render(request, 'properties/contact.html')

