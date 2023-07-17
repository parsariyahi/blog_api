from dataclasses import dataclass


@dataclass
class Settings:
    PROJECT_NAME: str = "Pars Bloggers"
    VERSION: str = "1.0.0"

settings = Settings()