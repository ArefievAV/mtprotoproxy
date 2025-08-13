import os

PORT = int(os.getenv("PORT", "8080"))
LISTEN_ADDR = "0.0.0.0"

SECRET = os.getenv("SECRET", "a1b2c3d4e5f60789aabbccddeeff0011")

USERS = {}

# Остальные параметры оставляем по умолчанию
