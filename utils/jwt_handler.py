def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'user_id1': user.id,
        'username': user.username,
        'token': token
    }

