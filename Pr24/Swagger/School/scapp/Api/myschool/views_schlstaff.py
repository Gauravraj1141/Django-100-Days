from django.shortcuts import render
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from scapp.Api.myschool.documentation_schlstaff import *


class SchlStaff(APIView):
    @swagger_auto_schema(
        tags=["User Property APIs"],
        # manual_parameters=[HEADER_PARAMS['access_token']],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=REQUIRED_LIST,
            properties=INPUT_PROPERTIES_DESCRIPTION),
        operation_description=OPERATIONS_DESCRIPTION,
        responses=GAURAV_DESCRIPT
    )
    def post(self, request):
        data = request.data
        return Response(data)
