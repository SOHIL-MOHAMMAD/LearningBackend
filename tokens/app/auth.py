import jwt
import datetime
from django.conf import settings
from django.utils import timezone
from .models import RefreshToken

def generate_access_token(user):
    payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15), # Short-lived access token
        "iat": datetime.datetime.utcnow()
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

def generate_refresh_token(user):
    expires_delta = datetime.timedelta(days=7) # Long-lived refresh token
    
    payload = {
        "user_id": user.id,
        "exp": datetime.datetime.utcnow() + expires_delta,
        "iat": datetime.datetime.utcnow()
    }
    
    # Generate the JWT string using a separate secret key
    token = jwt.encode(payload, settings.REFRESH_TOKEN_SECRET, algorithm="HS256")
    
    # Save to the database for revocation and reuse tracking
    RefreshToken.objects.create(
        user=user,
        token=token,
        expires_at=timezone.now() + expires_delta
    )
    
    return token