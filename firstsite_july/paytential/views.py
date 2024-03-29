# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
from paytential.models import Evaluation
from paytential.forms import EvaluationForm
# Create your views here.

def operation(request):
    return render(request, 'paytential/operationunit.html')

def login(request):
    return render(request, 'paytential/index3.html')

def contact(request):
    return render(request, 'paytential/login_with_correct_footer.html')

def help(request):
    return render(request, 'paytential/help.html')

def dashboard(request):
    return render(request, 'paytential/dashboard.html')

def create(request):
    return render(request, 'paytential/create_a_user.html')

def alogin(request):
    return render(request, 'paytential/admin_login_margin.html')

def odetails(request):
	return render(request, 'paytential/op_detail.html')

def ratings(request):

    if request.method == 'POST':
        form = EvaluationForm(data=request.POST)
        form.save()
    evaluation = Evaluation(user=request.user)
                            #this is a instance of the user model and also the current USER logged in

    form = EvaluationForm(instance=evaluation)
    users = User.objects.all()
    ratings = Evaluation.objects.all()

    return render(request, 'paytential/correct_rating.html', {'form': form, 'users':users, 'ratings':ratings,})
