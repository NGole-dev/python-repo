from seleniumpagefactory.Pagefactory import PageFactory

class HomePage(PageFactory):
    def __init__(self,driver):
        self.driver=driver
#https://bstackdemo.com/signin
    locators={
        "apple":('XPATH',"//span[contains(text(),'Apple')]"),
        "samsung":('XPATH',"//span[contains(text(),'Samsung')]"),
    }

    def click_apple(self):
        self.apple.click()

    def check_samsung(self):
        devicename=self.samsung.get_text()
        assert devicename=="amsung"
