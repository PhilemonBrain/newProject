from django.shortcuts import render
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.

# signin function


def signin(request):
    logger.info(request.POST)
