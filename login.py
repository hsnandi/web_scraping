from playwright.sync_api import sync_playwright
import time


class FlipkartLoginAutomation:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.browser = None
        self.page = None

    def start_browser(self):
        self.browser = sync_playwright().start().chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open_flipkart_login_page(self):
        self.page.goto("https://www.flipkart.com/account/login?ret=/")

    def enter_phone_number(self):
        self.page.wait_for_selector("input[type='text'][class*='r4vIwl']")
        self.page.fill("input[type='text'][class*='r4vIwl']", self.phone_number)

    def click_request_otp_button(self):
        self.page.click("button[class*='QqFHMw']")

    def wait_for_otp_input(self):
        self.page.wait_for_selector("div.XDRRi5 input[type='text'][class*='r4vIwl']")

    def get_user_otp_input(self):
        otp = input("Please enter the OTP received on your phone: ")
        return otp

    def enter_otp(self, otp: str):
        otp_fields = self.page.query_selector_all("div.XDRRi5 input[type='text'][class*='r4vIwl']")
        for i, field in enumerate(otp_fields):
            field.fill(otp[i])

    def wait_for_login_to_complete(self):
        try:
            self.page.wait_for_selector("div.yAlKeh", timeout=60000)
            print("Successfully logged in!")
        except Exception as e:
            print("Error: Could not detect successful login.")
            print(f"Details: {str(e)}")

    def navigate_to_profile_and_orders(self):
        self.page.goto("https://www.flipkart.com/account/orders")

    def close_browser(self):
        time.sleep(5)
        self.browser.close()


def main():
    phone_number = input("Please enter your phone number: ")
    flipkart_automation = FlipkartLoginAutomation(phone_number)

    flipkart_automation.start_browser()
    flipkart_automation.open_flipkart_login_page()
    flipkart_automation.enter_phone_number()
    flipkart_automation.click_request_otp_button()
    flipkart_automation.wait_for_otp_input()

    otp = flipkart_automation.get_user_otp_input()
    flipkart_automation.enter_otp(otp)
    flipkart_automation.wait_for_login_to_complete()
    flipkart_automation.navigate_to_profile_and_orders()
    flipkart_automation.close_browser()


if __name__ == "__main__":
    main()
