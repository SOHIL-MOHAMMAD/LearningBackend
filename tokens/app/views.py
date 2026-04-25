from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.decorators import (
    api_view,
    permission_classes
)
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import exceptions, status
from django.views.decorators.csrf import (
    ensure_csrf_cookie,
    csrf_protect
)

import jwt

from .serializer import (
    Userserializer,
    RegisterSerializer
)

from .auth import (
    generate_access_token,
    generate_refresh_token
)

from .models import RefreshToken


# -------------------
# PROFILE
# -------------------

@api_view(["GET"])
def profile(request):

    return Response({
        "user": Userserializer(
            request.user
        ).data
    })


# -------------------
# SIGNUP
# -------------------

@api_view(["POST"])
@permission_classes([AllowAny])
def signup_view(request):

    serializer = RegisterSerializer(
        data=request.data
    )

    if serializer.is_valid():
        user = serializer.save()

        return Response(
            {
              "message":"User created",
              "user":{
                 "id":user.id,
                 "username":user.username
              }
            },
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=400
    )


# -------------------
# LOGIN
# -------------------

@api_view(["POST"])
@permission_classes([AllowAny])
@ensure_csrf_cookie
def login_view(request):

    User = get_user_model()

    username = request.data.get(
        "username"
    )

    password = request.data.get(
        "password"
    )

    if not username or not password:
        raise exceptions.AuthenticationFailed(
            "Username and password required"
        )

    user = User.objects.filter(
        username=username
    ).first()

    if not user:
        raise exceptions.AuthenticationFailed(
            "User not found"
        )

    if not user.check_password(password):
        raise exceptions.AuthenticationFailed(
            "Wrong password"
        )


    access_token = generate_access_token(
        user
    )

    refresh_token = generate_refresh_token(
        user
    )


    response = Response({
        'refresh_Token' : refresh_token,
        "access_token":access_token,
        "user":Userserializer(
            user
        ).data
    })


    response.set_cookie(
        key="refreshtoken",
        value=refresh_token,
        httponly=True,
        secure=False,
        samesite="Lax"
    )

    return response


# -------------------
# REFRESH ROTATION
# -------------------

@api_view(["POST"])
@permission_classes([AllowAny])
@csrf_protect
def refresh_token_view(request):

    old_token = request.COOKIES.get(
        "refreshtoken"
    )

    if not old_token:
        raise exceptions.AuthenticationFailed(
            "No refresh token"
        )

    try:
        stored_token = RefreshToken.objects.get(
            token=old_token
        )

    except RefreshToken.DoesNotExist:
        raise exceptions.AuthenticationFailed(
            "Invalid refresh token"
        )


    # reuse detection
    if stored_token.is_revoked:

        RefreshToken.objects.filter(
            user=stored_token.user
        ).update(
            is_revoked=True
        )

        raise exceptions.AuthenticationFailed(
            "Token reuse detected"
        )


    try:
        jwt.decode(
            old_token,
            settings.REFRESH_TOKEN_SECRET,
            algorithms=["HS256"]
        )

    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed(
            "Refresh expired"
        )


    user = stored_token.user


    stored_token.is_revoked=True
    stored_token.save()


    new_access = generate_access_token(
        user
    )

    new_refresh = generate_refresh_token(
        user
    )


    response=Response({
       "access_token":new_access
    })


    response.set_cookie(
       key="refreshtoken",
       value=new_refresh,
       httponly=True,
       secure=True,
       samesite="Strict"
    )

    return response


# -------------------
# LOGOUT
# -------------------

@api_view(["POST"])
def logout_view(request):

    token=request.COOKIES.get(
        "refreshtoken"
    )

    if token:
        RefreshToken.objects.filter(
            token=token
        ).update(
            is_revoked=True
        )


    response=Response({
       "message":"Logged out"
    })

    response.delete_cookie(
        "refreshtoken"
    )

    return response