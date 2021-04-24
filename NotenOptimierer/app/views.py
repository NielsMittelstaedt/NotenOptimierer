from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from .solver import Solver
from .forms import SubjectForm

@csrf_exempt
def index(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        
        print(json_data["progra"])

        data={
            'name': 'Nikals'
        }
        return JsonResponse(data)

    form = SubjectForm()
    return render(request, 'app/form.html', {'form': form})