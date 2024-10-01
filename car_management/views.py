from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Car
from .forms import CarForm

# Create your views here.
def car_list(request):
	cars = Car.objects.all()

	# Filtering
	brand_filter = request.GET.get('brand')
	if brand_filter:
		cars = cars.filter(brand__icontains=brand_filter)

	price_filter = request.GET.get('price')
	if price_filter:
		cars = cars.filter(rental_price_per_day__lte=price_filter)

	availability_filter = request.GET.get('availability')
	if availability_filter:
		cars = cars.filter(availability=True if availability_filter == 'true' else False)

	# Pagination (10 cars per page)
	paginator = Paginator(cars, 10)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	context = {
		'page_obj': page_obj,
	}		

	return render(request, 'car_management/car_list.html', context)



def register_car(request):
	if request.method == 'POST':
		form = CarForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('car_list') # redirect to car list after submission
	else:
		form = CarForm()

	return render(request, 'car_management/register_car.html', {'form': form})		