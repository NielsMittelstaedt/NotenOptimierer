from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app.solver import Solver

def index(request):
    solver = Solver("test")
    solver.setupSolver()
    solver.solve()
    return render(request, 'app/index.html', {'name': "niklas"})