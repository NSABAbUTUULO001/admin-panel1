from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("http://localhost:3000/")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("http://localhost:3000/dashboard")
    page.screenshot(path="jules-scratch/verification/dashboard.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
