import json
import time

import pytest
from playwright.sync_api import Playwright, expect

from pages.dashBoardPage import dashboardPage
from pages.loginPage import LoginPage
from pages.ordersHistoryPage import OrdersHistoryPage
from utils.apiBase import APIUtils

# JSON file ->utils access into test

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "data", "credentials.json")

with open(file_path) as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize("user_credentials", user_credentials_list)
def test_e2e_Web_API(playwright: Playwright, user_credentials, browserInstance):
    # Create order using API
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)

    UserName = user_credentials["userEmail"]

    Password = user_credentials["userPassword"]

    # Create object of Login class for pageObject

    loginpage = LoginPage(browserInstance)

    loginpage.navigate(UserName, Password)

    dashboardpage = loginpage.navigate(UserName, Password)

    dashboardpage.selectOrdersNavLink()

    ordershistorypage = dashboardpage.selectOrdersNavLink()

    orderdetailspage = ordershistorypage.selectOrder(order_id)

    orderdetailspage.verifyOrderMessage()
