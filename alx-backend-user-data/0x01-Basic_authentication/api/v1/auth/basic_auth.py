#!/usr/bin/env python3
"""
Module for Basic Authentication
"""
from base64 import b64decode
import uuid
from typing import Optional, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Class that handles basic authentication
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
      """
      returns the Base64 part of the Authorization header for a Basic Authentication

      'Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=='

          username='Johnson'
          :
          password='pass'

          credentials = Johnson:pass

          QWxhZGRpbjpvcGVuIHNlc2FtZQ==
      """
      # Return None if authorization_header is None
      if authorization_header is None:
          return
      # Return None if authorization_header is not a string
      if not isinstance(authorization_header, str):
          return
      # Return None if authorization_header doesn’t start by Basic (with a space at the end)
      if not authorization_header.startswith('Basic '):
          return
      # Otherwise, return the value after Basic (after the space)
      value = authorization_header.split(' ')[1]
      return value
      # You can assume authorization_header contains only one Basic

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:  # noqa
        """
        returns the decoded value of a Base64 string base64_authorization_header

        QWxhZGRpbjpvcGVuIHNlc2FtZQ==

        Johnson@example.com:pass
        """
        # Return None if base64_authorization_header is None
        if not base64_authorization_header:
            return
        # Return None if base64_authorization_header is not a string
        if not isinstance(base64_authorization_header, str):
            return
        # Return None if base64_authorization_header is not a valid Base64
        # - you can use try/except
        try:
            encoded_base64 = b64decode(base64_authorization_header)
            decoded_base64 = encoded_base64.decode('utf-8')
        except Exception:
            return
        return decoded_base64

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> Optional[tuple[str, str]]:
        """
        returns the user email and password from the Base64 decoded value.

        Johnson@example.com:pass:sw:ws

        Johnson@example.com, pass
        """
        # This method must return 2 values, a tuple
        # Return (None, None) if decoded_base64_authorization_header is None
        if not decoded_base64_authorization_header:
            return None, None
        # Return (None, None )if decoded_base64_authorization_header is not a string
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        # Return (None, None) if decoded_base64_authorization_header doesn’t contain ':'
        if ":" not in decoded_base64_authorization_header:
            return None, None
        # Otherwise, return the user email and the user password - these 2 values must be
        #  separated by a :
        # You can assume decoded_base64_authorization_header will contain only one :
        # for now, cos a password could contain special character like a colon
        user, pwd = decoded_base64_authorization_header.split(':', maxsplit=1)
        return user, pwd
    
    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):  # noqa
        """
        Returns the User instance based on his email and password.

        user_email = Johnson@gmail.com
        user_pwd = pass
        """
        # Return None if user_email is None or not a string
        if not user_email or not isinstance(user_email, str):
            return
        # Return None if user_pwd is None or not a string
        if not user_pwd or not isinstance(user_pwd, str):
            return
        # Return None if your database (file) doesn’t contain any User instance with email
        # equal to user_email - you should use the class method search of the User to lookup the
        # list of users based on their email. Don’t forget to test all cases:
        # “what if there is no user in DB?”, etc.
        try:
            users = User.search(attributes={"email": user_email})
        except KeyError:
            return
        except Exception:
            return

        # Return None if user_pwd is not the password of the User instance found
        # - you must use the method is_valid_password of User
        if not users:
            return
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        # Otherwise, return the User instance
        return

    def current_user(self, request=None) -> TypeVar('User'):
        """
        verloads Auth and retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        # 'Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ=='
        b64_str = self.extract_base64_authorization_header(auth_header)
        # QWxhZGRpbjpvcGVuIHNlc2FtZQ==
        decoded_b64_str = self.decode_base64_authorization_header(b64_str)
        # Johnson@example.com:pass
        email, pwd = self.extract_user_credentials(decoded_b64_str)
        # Johnson@example.com, pass
        user = self.user_object_from_credentials(email, pwd)
        return user


if __name__ == '__main__':
    pass
