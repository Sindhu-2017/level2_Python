from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

EMPLOYEE_FILE = DATA_DIR / os.getenv("EMPLOYEE_FILE")
SALARY_FILE = DATA_DIR / os.getenv("SALARY_FILE")