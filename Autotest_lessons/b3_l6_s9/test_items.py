import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    try:
        # Open link in web driver
        browser.get(link)
        # Find a basket button on the page
        button_basket = browser.find_element_by_class_name('btn-add-to-basket')
        assert button_basket is not None, 'ERROR: Button basket is NOT found'
    finally:
        time.sleep(3)
