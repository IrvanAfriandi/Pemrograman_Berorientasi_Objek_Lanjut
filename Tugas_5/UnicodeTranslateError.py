text = "Halo, 世界"
try:
    encoded_text = text.encode('ascii')
except UnicodeTranslateError as e:
    print(f"UnicodeTranslateError: {e}")
