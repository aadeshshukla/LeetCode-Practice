import time
import hmac
import hashlib
import struct
import base64

def generate_totp(email):
    secret = (email + "HENNGECHALLENGE004").encode()
    
    timestep = 30
    T = int(time.time() // timestep)
    
    msg = struct.pack(">Q", T)
    h = hmac.new(secret, msg, hashlib.sha512).digest()
    
    offset = h[-1] & 0x0F
    code = struct.unpack(">I", h[offset:offset+4])[0] & 0x7fffffff
    otp = code % (10**10)
    
    return str(otp).zfill(10)

email = "aadeshshukla470@gmail.com"
otp = generate_totp(email)

auth_string = f"{email}:{otp}"
auth_base64 = base64.b64encode(auth_string.encode()).decode()

print("TOTP:", otp)
print("Authorization Header:")
print(f"Authorization: Basic {auth_base64}")

# This script generates a TOTP based on the provided   email and a secret key, then encodes the email and TOTP in Base64 for use in an HTTP Authorization header.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 