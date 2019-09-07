from django.shortcuts import render,HttpResponse
from .forms import fibForm
import time

# Create your views here.

def fibView(request):
    if request.method == 'POST':
        start_time = time.time()
        form = fibForm(request.POST)
        if form.is_valid():
            inputvar = form.cleaned_data['EnterNumber']
            fibonacci_numbers = [0, 1]
            for i in range(2, 1000):
                fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
        end_time = time.time() - start_time
        return HttpResponse('<h2> output fibonacci number u want is </h2><h1>{}</h1><h3>{}</h3>'.format(fibonacci_numbers[inputvar],end_time))
    else:
        print('hello')
        form = fibForm(request.GET)
        return render(request,'home.html',{'form':form})