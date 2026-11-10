"""Credential rotation test (Project 2, step 4).
Needs app.py running. Gets a short-lived M2M token, calls /api/chat (expect 200),
waits for the token to expire, replays the same token (expect 401).
"""
import os
import time
from datetime import datetime
import jwt
import requests
from dotenv import load_dotenv
load_dotenv(os.environ.get("ENV_FILE", ".env"))
DOMAIN = os.environ["AUTH0_DOMAIN"]
AUDIENCE = os.environ.get("M2M_AUDIENCE") or os.environ["API_AUDIENCE"]
BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:5000")

def ts():
   return datetime.now().astimezone().isoformat(timespec="seconds")

def call_chat(token, label):
   r = requests.post(
       f"{BASE_URL}/api/chat",
       headers={"Authorization": f"Bearer {token}"},
       json={"message": "hello from the agent"},
       timeout=10,
   )
   print(f"[{ts()}] {label}: HTTP {r.status_code} {r.text.strip()}")
   return r.status_code

resp = requests.post(
   f"https://{DOMAIN}/oauth/token",
   json={
       "grant_type": "client_credentials",
       "client_id": os.environ["M2M_CLIENT_ID"],
       "client_secret": os.environ["M2M_CLIENT_SECRET"],
       "audience": AUDIENCE,
   },
   timeout=10,
)
if resp.status_code != 200:
   raise SystemExit(f"[{ts()}] Auth0 token request failed: HTTP {resp.status_code} {resp.text}")   
body = resp.json()
token = body["access_token"]
claims = jwt.decode(token, options={"verify_signature": False})
lifetime = claims["exp"] - claims["iat"]
print(f"[{ts()}] M2M token issued, expires_in={body.get('expires_in')}s, exp-iat={lifetime}s")
call_chat(token, "fresh token ")           # expect 200
wait = lifetime + 2
print(f"[{ts()}] waiting {wait}s for the token to expire...")
time.sleep(wait)
call_chat(token, "expired token")  
