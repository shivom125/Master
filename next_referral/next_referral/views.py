from django.contrib.auth.decorators import login_required
from django.db.models import Subquery, OuterRef
from django.views.decorators.http import condition
from django.http import FileResponse, JsonResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaulttags import register
from django.template import loader
from django.contrib import messages
from django.http import StreamingHttpResponse
from django import template
from operator import itemgetter
from collections import defaultdict
from django.core.cache import cache
from threading import Thread
from django.db.models import Case, When, Count, IntegerField, CharField, DateTimeField
from django.db.models.functions import Cast
from django.core.paginator import Paginator

# @login_required(login_url="/login/")
def index(request):
    context={}
    return render(request,'index.html',context)
