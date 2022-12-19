from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import FF
from sklearn.linear_model import LinearRegression

# Create your views here.
def index(request):
    return render(request,'webapp/index.html')
def process(request):
    version = request.POST['version']
    csvfiles = FF.objects.get(id=2)
    data = pd.read_csv(csvfiles.fil)
    model = LinearRegression()
    model.fit(data[['version']], data[['price']])
    ans = model.predict([[int(version)]])
    ans2 = -1
    for a in ans:
        for x in a:
            ans2 = x
    return render(request,'webapp/index.html',{'version':ans2,'model':version})