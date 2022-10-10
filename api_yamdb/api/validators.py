from rest_framework import serializers, status
from rest_framework.exceptions import (
    APIException,
)


class NotFoundValidationError(APIException):
    status_code = status.HTTP_404_NOT_FOUND


def username_restriction(username):
    if username == 'me':
        raise serializers.ValidationError(
            'Not allowed to use "me" as username'
        )
    return username
