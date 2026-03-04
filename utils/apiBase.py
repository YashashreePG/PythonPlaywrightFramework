from playwright.sync_api import Playwright

ordersPayLoad = {"orders": [{"country": "India", "productOrderedId": "6960eac0c941646b7a8b3e68"}]}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data={"userEmail": user_credentials["userEmail"],
                                                  "userPassword": user_credentials["userPassword"]})
        assert response.ok
        print(response.json())
        responsebody = response.json()
        return responsebody["token"]

    def createOrder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order", data=ordersPayLoad,
                                            headers={"Authorization": token, "Content-type": "application/json"})
        print(response.json())
        response_body = response.json()
        order_id = response_body["orders"][0]
        return order_id

#This is a git comment for git
