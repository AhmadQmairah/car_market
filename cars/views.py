from django.shortcuts import render
from .models import Car
from .froms import CarForm
from django.shortcuts import redirect
from django.contrib import messages

def car_list(request):
	
	
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form=CarForm()
	if request.method=="POST":
		form=CarForm(request.POST,request.FILES)
		if(form.is_valid()):
			car=form.save()
			messages.success(request, 'Car Created')
			return redirect(car)

	context={"form":form}

	return render(request,'car_create.html',context)


def car_update(request, car_id):
	car=Car.objects.get(id=car_id)
	form=CarForm(instance=car)
	
	if request.method=="POST":
		form=CarForm(request.POST,request.FILES,car,instance=car)
		if(form.is_valid()):
			car=form.save()
			messages.success(request, 'Car Updated.')
			return redirect(car)

	context={"form":form}

	return render(request,'car_create.html',context)


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.success(request, 'Car Deleted.')
	return redirect("car-list")