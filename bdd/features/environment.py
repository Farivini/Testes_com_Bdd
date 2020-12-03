from selenium import webdriver

def before_all(context):
    PATH = 'C:\Program Files (x86)\chromedriver.exe' 
    context.web = webdriver.Chrome(PATH)


def after_step(context, step):
    pass


def after_all(context):
    pass
