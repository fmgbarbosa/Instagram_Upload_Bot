from selenium.import webdriver as webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime,date
import time
import random
import pandas
import autoit
import numpy

#Nota: Pip install xlrd!!!!!!!!!!!!!!!!!!!!!

def initiate_mobile_webdriver():
    global webdriver
    chromedriver_path = '<path to chomedriver.exe>'
    mobile_emulation = {"deviceName":"Pixel 2"}
    opts=wb.ChromeOptions()
    opts.add_experimental_option{"mobileEmulation",mobile_emulation}
    webdriver = wb.Chrome(executabe_path=chromedriver_path,options=opts)
    time.sleep(2)

def login(user_info,pass_info):
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    time.sleep(3)
    username = webdriver.find_element_by_name('username')
    username.send_keys(user_info)
    time.sleep(1.5)
    password=webdriver.find_element_by_name('password')
    password.send_keys(pass_info)
    time.sleep(2.3)
    button_login = webdriver.find_element_by_xpath('<xpath for element login>')
    button_login.click()

def close_data_not()
    try:
        time.sleep(1.5)
        notification=webdriver.find_element_by_css_selector('#react-root>section>main>div>button')
        notification.click()
    except:
        pass

def close_homescreen_not()
    try:
        time.sleep(1.2)
        home_screen=webdriver.find_element_by_css_selector('<insert css selector>')
        home_screen.click()
    except:
        pass

def close_activ_not()
    try:
        time.sleep(1.5)
        notif=webdriver.find_element_by_xpath('<insert xpath>')
        notif.click()
    except:
        pass


def upload_photo(image_path,caption)
    #upload file
    time.sleep(3)
    new_post_button=webdriver.find_element_by_xpath('<insert xpath for button>').click()
    time.sleep(1.5)
    
    #janela windows -> autoit
    autoit.win_activate('Abrir')
    time.sleep(2)
    autoit.control_send("Abrir","Edit1",image_path)
    time.sleep(1.5)
    autoit.control_send("Abrir","Edit1","{ENTER}")

    #Avançar Página
    time.sleep(2)
    next_button = webdriver.find_element_by_xpath("<insert xpath>").click()

    #Adicionar Caption/Legenda
    time.sleep(3)
    legenda = webdriver.find_element_by_xpath("<insert xpath>")
    legenda.send_keys(caption)

    #partilhar
    time.sleep(2)
    share_button = webdriver.find_element_by_xpath("<insert xpath>").click()

def get_posts():
    #Identificar posts mais recentes
    df = pandas.read_excel(r"<insert caminho para o ficheiro excel>")
    curr_datetime=datetime.now() #data e hora atual

    #Eliminar se publish_datetime<curr_datetime
    df['publish_datetime'] = pandas.to_datetime(df['publish_datetime'])
    df = df[df.publish_datetime>curr_datetime]
    df = df.sort_values('publish_datetime',ascending=True)
    df = df.reset_index(drop=True)

    return df

def main():
    while True:
        post = get_posts()
        print('Post Publish Date',post.publis_datetime[0])
        time.sleep(1*60)
        curr_datetime = datetime.now()

        #Publicar se o publish_datetime[0]<datetime
        if post.publish_datetime[0]<curr_datetime:
            user_info = '<insert username>'
            pass_info = '<insert password>'
            
            #Abrir Browser
            initiate_mobile_webdriver()
            login(user_info,pass_info)

            #Fechar Popup
            close_data_not()
            close_homescreen_not()
            close_activ_not()

            #Publicar
            image_path = post.image_path[0]
            legenda = post.caption[0]
            upload_photo(image_path,legenda)
            time.sleep(25)

            #Fechar Browser
            webdriver.close()

if __name__ == "__main__":
    main()


# Done!!!!!!! :)



