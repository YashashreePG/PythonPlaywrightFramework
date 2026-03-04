from pages.dashBoardPage import dashboardPage


class LoginPage:

    def __init__(self,page):
         self.page = page


    def navigate(self,UserName,Password):
        self.page.goto("https://rahulshettyacademy.com/client")
        self.page.locator("#userEmail").fill(UserName)
        self.page.locator("#userPassword").fill(Password)
        self.page.get_by_role("button", name="Login").click()
        dashboardpage = dashboardPage(self.page)
        return dashboardpage


