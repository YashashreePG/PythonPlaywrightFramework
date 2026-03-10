import os

import pytest
from playwright.sync_api import Playwright
from playwright.sync_api import sync_playwright
import pytest_html


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Browser name: chrome or firefox"
    )


@pytest.fixture
def browserInstance(playwright: Playwright, request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=True)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=True)

    context = browser.new_context(
        record_video_dir="videos/"
    )
    page = context.new_page()
    yield page

    #-----------------test finished------------
    video = page.video
    page.close()
    context.close()
    browser.close()

    if video:
        request.node.video_path = video.path()

    #
    # if video:
    #     try:
    #         video_path = video.path()
    #         print("video_path" , video.path())
    #         request.node.video_path = str(video_path)
    #     except :
    #         request.node.video_path = None










