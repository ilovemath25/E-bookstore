from flask import request
from hashlib import sha256
import json
from datetime import datetime
   
def load_sessions():
   with open("ebookstore_flask/utils/sessions.json", 'r') as f: return json.load(f)

def add_session(email, mid, role):
   session_store = load_sessions()
   session_id = generate_session(email, mid)
   session_store[session_id] = [email, role]
   with open("ebookstore_flask/utils/sessions.json", 'w') as f: json.dump(session_store, f, indent=3)
   return session_id

def check_session():
   session_id = request.cookies.get("session_id")
   if session_id and session_id in load_sessions(): return True
   return False

def generate_session(email, mid):
   today_date = datetime.now().strftime("%Y-%m-%d")
   session_string = email + str(mid) + str(today_date)
   return sha256(session_string.encode('utf-8')).hexdigest()