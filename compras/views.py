# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone


from django.shortcuts import render
from compras.models import Compras

# Create your views here.
def dame_compras(request):
    context = {}
    context['compras'] = Compras.objects.all()
    return render(request, 'comras.html', context)

def mostrar(request):
    context = request.POST.get('texto')
    compra = Compras(texto=context)
    compra.save()
    return redirect('/')

def eliminar(request):
    context = request.POST.get('compra_id')
    compra = Compras.objects.get(id=context)
    compra.delete()
    return redirect('/')

def archivar(request):
    context = request.POST.get('compra_id')
    compra = Compras.objects.get(id=context)
    compra.archived = True
    compra.save()
    return redirect('/')
    