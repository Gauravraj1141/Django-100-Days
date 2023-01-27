# from django.shortcuts import render
# from rest_framework.views import APIView
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework.response import Response


# class SchlStaff(APIView):
#     @swagger_auto_schema(
#         tags=["User Property APIs"],
#         manual_parameters=[HEADER_PARAMS['access_token']],
#         request_body=openapi.Schema(
#             type=openapi.TYPE_OBJECT,
#             required=REQUIRED_LIST,
#             properties=INPUT_PROPERTIES_DESCRIPTION),
#         operation_description=OPERATIONS_DESCRIPTION,
#         responses=RESPONSE_DESCRIPTION
#     )
#     def get(self, request):
#         x = 444
#         return Response("Hey it is ", x)

#     def post(self, request, id):
#         return Response(id)
