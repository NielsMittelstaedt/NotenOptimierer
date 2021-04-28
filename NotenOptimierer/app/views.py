from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
from .solver import Solver
from .forms import SubjectForm

import random

@csrf_exempt
def index(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        
        thesis = (1.0, 22.5)
        solver = Solver([], thesis)
        best_node = solver.solve()
        print(best_node)
        data={
            'name': 'Nikals'
        }

        return JsonResponse(data)


    form = SubjectForm()
    return render(request, 'app/form.html', {'form': form})

@csrf_exempt
def informatik(request):
    # Return a list of all values needed for the calculation
    if request.method == 'GET':
        json_data = json.load(open('assets/informatik.json'))
        return JsonResponse(json_data)