from django.shortcuts import render,get_list_or_404, get_object_or_404
from rest_framework import generics, renderers,status
from rest_framework.response import Response
import datetime, time, requests, json


from aplication.models import *
from aplication.serializers import *

# viewset rest
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ViewSetMixin
# import rest_framework

