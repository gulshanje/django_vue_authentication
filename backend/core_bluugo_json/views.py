
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from .models import Vehicle
from .forms import JsonUploadForm
from django.core.paginator import Paginator

def upload_view_json(request):
    if request.method == 'POST':
        form = JsonUploadForm(request.POST, request.FILES)
        if form.is_valid():
            json_file = request.FILES['json_file']
            data = json.load(json_file)
            new_data = []
            for item in data:
                if not Vehicle.objects.filter(model_year=item['model_year'], make=item['make'], model=item['model'],
                                              rejection_percentage=item['rejection_percentage'],
                                              reason_1=item['reason_1'],reason_2=item['reason_2'],reason_3=item['reason_3']).exists():
                    new_data.append(Vehicle(model_year=item['model_year'], make=item['make'], model=item['model'],
                                              rejection_percentage=item['rejection_percentage'],
                                              reason_1=item['reason_1'],reason_2=item['reason_2'],reason_3=item['reason_3']))
            Vehicle.objects.bulk_create(new_data)
            
            return redirect('upload_view_json')
    else:
        form = JsonUploadForm()

    vehicle_list = Vehicle.objects.all()
    paginator = Paginator(vehicle_list, 50)  # Show 10 people per page

    page_number = request.GET.get('page')
    vehicles = paginator.get_page(page_number)
    return render(request, 'core_bluugo_json/upload_view_json.html', {'form': form, 'vehicles': vehicles})


