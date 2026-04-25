import jwt

from rest_framework.authentication import (
    BaseAuthentication
)

from rest_framework import exceptions

from django.contrib.auth import get_user_model
from django.conf import settings


class SafeJWTAuthentication(
    BaseAuthentication
):

    def authenticate(
        self,
        request
    ):

        auth_header = request.headers.get(
            "Authorization"
        )

        if not auth_header:
            return None


        try:
            parts = auth_header.split()

            if len(parts) != 2:
                raise exceptions.AuthenticationFailed(
                    "Invalid header"
                )

            if parts[0].lower() != "bearer":
                raise exceptions.AuthenticationFailed(
                    "Bearer token required"
                )

            token = parts[1]

            payload = jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                "Access token expired"
            )


        User = get_user_model()

        user = User.objects.filter(
            id=payload["user_id"]
        ).first()


        if not user:
            raise exceptions.AuthenticationFailed(
                "User not found"
            )

        return (user,None)