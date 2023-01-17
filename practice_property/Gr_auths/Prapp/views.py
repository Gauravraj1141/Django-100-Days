
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PrForm
from .models import PropertyDetail, State, City


#  add our property

def All_Property(request):
    if request.method == "POST":
        formdata = PrForm(request.POST)
        if formdata.is_valid():
            propertyname = formdata.cleaned_data["Property_name"]
            propertyaddress = formdata.cleaned_data["Property_address"]
            propertstate = formdata.cleaned_data["State_name"]
            propertycity = formdata.cleaned_data["City_name"]
            PropertyDetail.objects.create(
                Property_name=propertyname, Property_address=propertyaddress, City_name=propertycity, City_name__state=propertstate)
            messages.success(request, 'Your Property added Successfully!')
            return redirect("/")
    else:
        formdata = PrForm()

    # fetch all properties
    Properties = PropertyDetail.objects.all()

    context = {"form": formdata, "Porperties": Properties}
    return render(request, 'pr_app/Home.html', context)


# update property details


def Update_Property(request, id):
    Pr_data = PropertyDetail.objects.get(Pr_id=id)
    if request.method == "POST":
        formdata = PrForm(request.POST, instance=Pr_data)
        if formdata.is_valid():
            formdata.save()
            messages.success(request, "Your Property Updated Successfully!")
            return redirect("/")

    else:
        formdata = PrForm(instance=Pr_data)
    context = {"form": formdata}
    return render(request, "pr_app/Update.html", context)


# Fetch property by city name


def Fetch_Property(request):
    if request.method == "POST":
        cityname = request.POST['city']
        properties = PropertyDetail.objects.filter(City_name__ctname=cityname)
        context = {"properties": properties}
        return render(request, 'pr_app/Fetch_pr.html', context)

    return render(request, 'pr_app/Fetch_pr.html')


# fetch cities by state


def Find_cities(request):
    if request.method == "POST":
        statename = request.POST['state']
        cities = PropertyDetail.objects.filter(State_name__stname=statename)

        context = {"cities": cities}
        return render(request, 'pr_app/Find_city.html', context)

    return render(request, 'pr_app/Find_city.html')


# find all similiar city name properties by propertyid

def Find_similiar_pr(request):
    if request.method == "POST":
        pr_id = request.POST['id']
        try:
            pr_data = PropertyDetail.objects.get(Pr_id=pr_id)
        except Exception:
            messages.warning(request, "Please give a valid id ! ")
            return redirect("Find_similiar")
        cityname = pr_data.City_name
        similiar_data = PropertyDetail.objects.filter(City_name=cityname)
        context = {"Similiar_city_data": similiar_data}
        return render(request, 'pr_app/Find_similiar.html', context)

    return render(request, 'pr_app/Find_similiar.html')


# fetch city for showing to the user


def get_cities(request):
    state_id = request.GET.get('state_id')
    cities = City.objects.filter(
        state__st_id=state_id).values('ct_id', 'ctname')
    return JsonResponse({'cities': list(cities)})
