import os
import dotenv

dotenv.load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USERNAME =  os.getenv("MYSQL_USERNAME")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_QUERY = {
  "charset": "utf8mb4",
  "collation": "utf8mb4_unicode_ci"
}
