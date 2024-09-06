
import os
from dotenv import load_dotenv

load_dotenv('.env')
my_user = os.getenv('user_name')
my_pass = os.getenv('password')