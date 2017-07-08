# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from get_data import Data


# Create your views here.
@api_view(["GET"])
def get_data_gps(request):
    try:
        obj = Data()
        result = obj.get_gps_data()
        #
        # result  = {
        #     "geometry":{
        #         "type": "Point",
        #         "coordinates": [53.428361, -1.37398]
        #     },
        #     "type": "Feature",
        #     "properties": {}
        # }


        # result = {"sunny":123}
        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        print e.message
