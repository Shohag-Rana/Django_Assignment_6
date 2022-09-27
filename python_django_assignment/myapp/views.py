from django.shortcuts import render
from . models import Property, Category, Location
from django.db.models import Max, Min
from django.core.paginator import Paginator

# Create your views here.
def home_page(request):
    min_price = Property.objects.aggregate(Min('price')) # find the minimum price of the Property table
    max_price = Property.objects.aggregate(Max('price')) # find the maximum price of the Property table
    properties = Property.objects.all()
    # default value set 
    location = None
    price_range = min_price['price__min']
    filter_value = "low_to_high"

    if request.method == 'POST':
        price_range = request.POST['range']
        location_text = request.POST['search']
        filter_value = request.POST['filter_value'] # filter value --> low to high, high to low

        if location_text:
            location = (Location.objects.filter(location_name__icontains = location_text)) # search location from the location table if find return an object


        if location:
            location = location[0]
            if filter_value == "high_to_low":
                # Filter the property table data based on search location and price descending order
                properties = Property.objects.filter(price__gte = price_range, location_id = location).order_by('-price')
            else:
                # Filter the property table data based on search location and price ascending order
                properties = Property.objects.filter(price__gte = price_range, location_id = location).order_by('price')

        else:
            if filter_value == "high_to_low":
                # Filter the property table data based on price descending order
                properties = Property.objects.filter(price__gte = price_range).order_by('-price')
            else:
                # Filter the property table data based on price ascending order
                properties = Property.objects.filter(price__gte = price_range).order_by('price')

    # append the property and category data in list [key, value] order for pagination operation
    datas = list()
    for property in properties:
        category = Category.objects.filter(property_id = property)
        datas.append((property, category))

    # paginate 5 datas in per page 
    paginator = Paginator(datas, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # access url filter data 
    find_location = request.GET.get('location')
    price = request.GET.get('price')
    filter_data = request.GET.get('filter')
    print(find_location, price, filter_data)
  
    if page_obj.has_next():
        print(paginator.get_page(page_obj.next_page_number()))
    if page_obj.has_previous():
        print(page_obj.previous_page_number())
        
    context = {
        'min_price': min_price['price__min'],
        'max_price': max_price['price__max'],
        'page_obj': page_obj,
        'location': location,
        'price_range': price_range,
        'filter_value': filter_value
    }
    return render(request, 'home.html', context)




