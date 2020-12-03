from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import urllib.request
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@given(u' que acesso a página do Audatex')
def step_impl(context):
    PATH = 'C:\Program Files (x86)\chromedriver.exe'                  #  CAMINHO DO EXECUTAVEL DRIVE DO GOOGLE
    drive = webdriver.Chrome(PATH)                                    # ASSINALANDO PARA A VARIAVEL
    drive.get("https://login.audatex.com.br/account/login?returnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Daudatexweb%26redirect_uri%3Dhttps%253A%252F%252Faudatexweb.audatex.com.br%252FAudatex_Home.aspx%26response_mode%3Dform_post%26response_type%3Dcode%2520id_token%26scope%3Dopenid%2520profile%2520offline_access%2520roles%2520usuario_info%2520usuario_detalhes%26state%3DOpenIdConnect.AuthenticationProperties%253DvqnSY24pqEKDaL5eILzcM8oxMNzs2O8_tdVeJ2baTtkn8etKS8_2KfejjphbRwE45DCvq8AMNbqgnSQ-HNbzyeKEvVFiefkXModr6mSNJTu-BSqjXoqlAC27juVSzeS6_4rWEBHYtetcL-RpQaRPS6-Mg263frUnthEAZ9saVmiZRoEJKz_NZFFDUCWeWDKnm6ttkFdOGK9sRjRuQzk1Ufq_o96ARqOsnPb2KzmVo1cllvDzHcbQZjKaAX4EYGJGFElfeQkWotQ8yygKvrPigkHgDvFZjJLdAYfV02DW54w%26nonce%3D637333160557911875.N2Q5NzllMjAtNTFjOC00Y2FiLWFlYTgtOTIxOWQ0MzcwOGEyNjQxZWFjMTUtMjg2MS00YjVhLTljZmUtMmJhMmUyN2I2YjBi%26x-client-SKU%3DID_NET%26x-client-ver%3D1.0.40306.1554")

@when(u'realizo loggin')
def  step_impl(context):
    usuario = drive.find_element_by_id("UserName")
    usuario.send_keys("coloco o USUSARIO")
    #acessando colocando a senha
    senha = drive.find_element_by_id("Password")
    senha.send_keys("COLOCO A SENHA")
    senha.send_keys(Keys.RETURN)   

@when(u'loggin e realizado')
def step_impl(context):
    pass

@then(u'o titulo da pagina deve ser verificado')
def step_impl(context):
    drive.title
