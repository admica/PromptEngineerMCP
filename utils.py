# PATH: utils.py
import re

def sanitize_string(s: str) -> str:
    """
    Remove problematic control characters (except newline and tab) and trim whitespace.
    """
    # Remove control characters: characters in the ranges \x00-\x08, \x0B-\x1F, and \x7F.
    return re.sub(r'[\x00-\x08\x0B-\x1F\x7F]', '', s).strip()

def sanitize_dict(d: dict) -> dict:
    """
    Recursively sanitize all string values in a dictionary.
    """
    sanitized = {}
    for key, value in d.items():
        if isinstance(value, str):
            sanitized[key] = sanitize_string(value)
        elif isinstance(value, dict):
            sanitized[key] = sanitize_dict(value)
        else:
            sanitized[key] = value
    return sanitized
