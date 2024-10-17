import os
from typing import Optional

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, ValidationError

# Load environment variables from the .env file
load_dotenv(dotenv_path=find_dotenv())


class Config(BaseModel):
    """Base Config for environment variables related to MySQL"""

    db_url: Optional[str]
    db_name: Optional[str]
    db_user: Optional[str]
    db_password: Optional[str]


# Create a Config instance from environment variables
try:
    config = Config(
        db_url=os.environ["DB_URL"],  # MySQL server URL
        db_name=os.environ["DB_NAME"],  # Database name
        db_user=os.environ["DB_USER"],  # MySQL username
        db_password=os.environ["DB_PASSWORD"],  # MySQL password
    )
except KeyError as e:
    raise KeyError(f"Missing environment variable: {e}")
except ValidationError as e:
    raise ValueError(f"Configuration error: {e}")
