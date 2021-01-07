from django.shortcuts import render
from .forms import TuristaForm
from django.http import HttpResponseRedirect
# Create your views here.
def novoTurista(request):
    form = TuristaForm(request.POST, None)

    if form.is_valid():
        form.save()

    return  render(request, 'Cadastro.html', {'form':form})
