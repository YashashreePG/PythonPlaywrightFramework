from pages.ordersHistoryPage import OrdersHistoryPage


class dashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNavLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        ordershistorypage = OrdersHistoryPage(self.page)
        return ordershistorypage
