text = "🌈💻🚀"
try:
    encoded_text = text.encode('ascii')
except UnicodeError as e:
    print(f"UnicodeError: {e}")
