from enum import Enum

from pydantic_settings import BaseSettings
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath

class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseSettings):
    email: EmailStr
    username: str
    password: str


class TestData(BaseSettings):
    image_png_file: FilePath


class Settings(BaseSettings):
    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath