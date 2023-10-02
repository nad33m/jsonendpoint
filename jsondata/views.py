from collections import Counter
from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.decoratorspytho import login_required
import requests
import json
from django.http import HttpResponse,JsonResponse
from datetime import datetime, timedelta
import csv
from .models import *
from django.db.models import Q, OuterRef, Subquery
from django.shortcuts import render
from django.utils.html import escape
from django.views import View
import re
from django.db.models import Sum,F
from django.utils.html import escape
from datetime import datetime, timedelta
from django.db.models import Count
# Create your views here.

from .models import *
# Create your views here.

def index(request): 
    url = "https://kc.humanitarianresponse.info/api/v1/data/1111365?format=json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if the request fails
    json_data = response.json()
    
    context = {
        'json_data': json_data,
    }

    return render(request, 'jsondata/index.html', context)