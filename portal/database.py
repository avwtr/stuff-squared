from deta import Deta
import os
from dotenv import load_dotenv
from datetime import datetime
import json
#load_dotenv()
DETA_KEY = "b0qx6lp9_9aQiywgU4zfT2Uu12efSRjzCXtt5mqGo"#os.environ.get('DETA_KEY')
portal = Deta(DETA_KEY)
portal_db = portal.Base("portal_usage")

def insert_case(prompt, datetime):
    return portal_db.put({"prompt": prompt, "datetime": datetime})