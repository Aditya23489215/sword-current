from django.shortcuts import render, redirect
from .learning import learning
from .models import Learning
from .forms import SalaryForm
import json

# Create your views here.
def learning_view(request):
    values = Learning.objects.all()
    new_values = [{'x':obj.x, 'y':obj.y} for obj in values]

    if request.method == "POST":
        form = SalaryForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            result = learning(age)
            form = SalaryForm()
            return render(request, 'artificial_intelligence/learning.html', {'form':form, 'age':age, 'value':result[0], 'coeff':result[1], 'intercept':result[2], "entries":json.dumps(new_values)})
    form = SalaryForm()
    result = learning(1)
    return render(request, 'artificial_intelligence/learning.html', {'form':form, 'coeff':result[1], 'intercept':result[2], "entries":json.dumps(new_values)})

def save_object(request, age):
    if request.method == 'POST':
        salary = float(request.POST.get('salary'))
        Learning.objects.create(x=age, y=salary)
        return redirect('learning')
    return redirect('learning')
