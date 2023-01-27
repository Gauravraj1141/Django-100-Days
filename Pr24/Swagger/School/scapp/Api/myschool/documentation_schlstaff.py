from drf_yasg import openapi


# Swagger Descriptions start here
# HEADER_PARAMS = {
#     'access_token': openapi.Parameter('accesstoken', openapi.IN_HEADER, description="local header param", type=openapi.IN_HEADER),
# }


SAMPLE_INPUT = {
    "authentication_params": {
        "number": "1"
    }
}

SAMPLE_RESPONSE_SUCCESS = {

    "Payload": {
        "number": [
            {
                "1"
            }

        ]
    }

}


OPERATIONS_DESCRIPTION = """ 
This function will return Notification.
**endpoint url:** baseurl/post_login/property_management/notification_for_hellow/
"""


INPUT_PROPERTIES_DESCRIPTION = {
    "authentication_params": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="required authentication params for lisitng",
        example={
            "number": "1"
        },


    )
}


REQUIRED_LIST = []

GAURAV_DESCRIPT = {
    '200': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Output if API successfully fetched  notification',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_STRING, description="Status code of API output", example=200),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status",
                                      example="notification_for_hellow service executed successfully with service_request_id as48b97ec8-9a68-11ed-aad9-089798bf41eb"),
            "Payload": openapi.Schema(
                type=openapi.TYPE_OBJECT, description="Show Notification",
                properties={
                    "notification": openapi.Schema(
                        type=openapi.TYPE_STRING,
                        example="Hellow World"
                    )
                }
            )


        }),
    '404':  openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description="Output if API doesn't fetched profile details",
        properties={
            "Status": openapi.Schema(
                type=openapi.TYPE_STRING,
                description="Status code of API output",
                example=404),
            "Message": openapi.Schema(type=openapi.TYPE_STRING,
                                      description="Description of status of API output",
                                      example="update_user_profile service"
                                              "with service_request_id ascfc1f659-fce2-11ec-b81b-70a6cc340b6f, "
                                              "could not be executed as given profile_id does not exist in database"
                                      ),
            "Payload": openapi.Schema(
                type=openapi.TYPE_OBJECT, description="The payload will always be an empty dictionary",
                properties={},
                example={}
            )
        }
    ),
    '452':  openapi.Schema(
        type=openapi.TYPE_OBJECT,
        description='Validation failure output',
        properties={
            "Status": openapi.Schema(type=openapi.TYPE_STRING, description="Status code of API output", example=452),
            "Message": openapi.Schema(type=openapi.TYPE_STRING, description="Description of API output status",
                                      example="user_profile' is a required property")
        }
    )
}

API_LOGIC = """ 
Step 1:
Step 2:
Step 3:
....

"""
# ################ Swagger Descriptions End here  #####################
