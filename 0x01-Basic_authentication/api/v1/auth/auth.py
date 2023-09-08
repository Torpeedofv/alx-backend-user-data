#!/usr/bin/env python3
"""A module for a class"""
from flask import request
from typing import List, TypeVar


class Auth:
    """auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns False"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if path.rstrip('/') == excluded_path.rstrip('/'):
                return False
            if path in excluded_paths:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns None"""
        return None
