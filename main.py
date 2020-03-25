import json
import time
import selenium
import pyautogui
from requests import get
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

def display_ip():
    ip = get('https://api.ipify.org').text
    print ('My public IP address is:', ip)


def twitterAutopost(USERNAME,PASSWORD, MESSAGE, driver):
    driver.get('http://www.twitter.com/login')

    try:
        emailElement = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input'))).send_keys(USERNAME)
        passwordElement = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input'))).send_keys(PASSWORD)
        time.sleep(2)
        loginElement = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div'))).click()

    except Exception as e:
        print(e)

    try:
        time.sleep(3)
        tweetWriteClicker = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]'))).click()
        tweetWriter = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'))).send_keys(message)
        tweetSender = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span'))).click()

        time.sleep(3)
        profileClicker = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div/div[2]/nav/a[7]/div').click()
        time.sleep(5)
        tweetClicker = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div/div[2]').click()

        currentUrl = driver.current_url
        with open('output.txt', 'a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)


def linkedinAutopost(USERNAME,PASSWORD,MESSAGE,driver):
    driver.get('http://www.linkedin.com/login')

    try:
        time.sleep(3)
        emailElement = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,'username'))).send_keys(USERNAME)
        passwordElement = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID,'password'))).send_keys(PASSWORD + Keys.ENTER)

    except Exception as e:
        print(e)

    try:
        time.sleep(3)
        linkedinWriter = driver.find_element_by_xpath('//*[@id="ember55"]/div/div[1]/button[1]').click()
        linkedinMessageWriter = driver.find_element_by_class_name("mentions-texteditor__contenteditable").send_keys(MESSAGE)
        messageSender = driver.find_element_by_xpath("//*[@data-control-name='share.post']").click()
        time.sleep(2)

        profileClicker = driver.find_element_by_xpath('//*[@id="ember23"]').click()
        time.sleep(1)
        profileClicker2 = driver.find_element_by_xpath('//*[@id="ember26"]/div[2]').click()
        time.sleep(3)

        tempUrl = driver.current_url
        activityUrl = tempUrl + "detail/recent-activity/"
        driver.get(activityUrl)

        with open('output.txt', 'a+') as f:
            f.write(activityUrl + "\n")

    except Exception as e:
        print(e)


def plurkAutopost (USERNAME,PASSWORD,MESSAGE, driver):
    driver.get('https://www.plurk.com/login?r=')

    try:
        usernameElement = driver.find_element_by_id("input_nick_name").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("input_password").send_keys(PASSWORD)
        loginSubmitElement = driver.find_element_by_id("login_submit").click()
        time.sleep(3)

        messageWriter = driver.find_element_by_id("input_big").send_keys(MESSAGE)
        time.sleep(1)
        messageSender = driver.find_element_by_class_name("submit_img").click()
        time.sleep(1)

        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)

def tumblrAutopost(EMAIL, PASSWORD, MESSAGE,driver ):
    driver.get('https://www.tumblr.com/login')

    try:
        emailElement = driver.find_element_by_id("signup_determine_email").send_keys(EMAIL)
        emailSubmit = driver.find_element_by_class_name("signup_determine_btn").click()
        time.sleep(2)
        confirmPassword = driver.find_element_by_class_name("forgot_password_link").click()
        passwordElement = driver.find_element_by_id("signup_password").send_keys(PASSWORD)
        loginButton = driver.find_element_by_class_name("signup_login_btn").click()

        time.sleep(3)
        messageSelector = driver.find_element_by_id("new_post_label_text").click()
        messageWriter = driver.find_element_by_class_name("editor-richtext").send_keys(MESSAGE)
        messageSender = driver.find_element_by_class_name("create_post_button").click()

        time.sleep(3)
        urlFinder = driver.find_element_by_id("account_button").click()
        time.sleep(3)
        postFinder = driver.find_element_by_class_name("blog-list-item-avatar-image").click()
        time.sleep(3)

        postLink = driver.current_url

        with open('output.txt','a+') as f:
            f.write(postLink + "\n")

    except Exception as e:
        print(e)


def scoopitAutopost (EMAIL, PASSWORD, MESSAGE, driver):
    driver.get('https://www.scoop.it/login')

    try:
        emailElement = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/input').send_keys(EMAIL)
        passwordElement = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input').send_keys((PASSWORD))
        submitLogin = driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/button').click()

        time.sleep(3)
        messageSelector = driver.find_element_by_id("urlChooserField").click()
        messageWriter = driver.find_element_by_id("urlChooserField").send_keys(MESSAGE)
        messageSender = driver.find_element_by_id("urlChooserButton").click()
        time.sleep(5)
        messagePublisher = driver.find_element_by_xpath('//*[@id="h_scoopitWindowPopup"]/div/div[2]/div/div[3]/div[3]/div/div').click()
        time.sleep(3)


        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)


def instapaperAutopost (USERNAME, PASSWORD, MESSAGE, driver):
    driver.get('https://www.instapaper.com')

    try:
        signinButton = driver.find_element_by_xpath('//*[@id="control_bar"]/div/nav/a[1]').click()
        emailElement = driver.find_element_by_id("sign_in_modal_email").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("password").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_id("register").click()

        time.sleep(5)
        messageSelector = driver.find_element_by_xpath('//*[@id="page_header"]/div[2]/div[1]/div[2]/section/div[2]/a[2]/span').click()
        messageWriter = driver.find_element_by_xpath('//*[@id="add_link_modal"]/div[3]/form/div/input[1]').send_keys(MESSAGE)
        messageSender = driver.find_element_by_xpath('//*[@id="add_link_modal"]/div[3]/form/div/input[2]').click()

        time.sleep(3)

        urlCopy = driver.find_element_by_class_name("article_title").click()
        time.sleep(3)
        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)


def livejournalAutopost (USERNAME,PASSWORD,MESSAGE,driver):
    driver.get("https://www.livejournal.com")

    try:
        loginButton = driver.find_element_by_xpath('//*[@id="js"]/body/div[2]/header/div/nav[2]/ul/li[2]/a').click()
        time.sleep(2)
        usernameElement = driver.find_element_by_id("user").click()
        usernameInput = driver.find_element_by_id("user").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("lj_loginwidget_password").send_keys(PASSWORD)
        submitLogin = driver.find_element_by_xpath('//*[@id="js"]/body/div[2]/div[3]/div/div[2]/form[1]/button').click()

        time.sleep(5)
        messageSelector = driver.find_element_by_xpath('//*[@id="js"]/body/div[2]/header/div/nav[2]/ul/li[3]/a/span[1]').click()
        time.sleep(5)
        messageClick = driver.find_element_by_xpath('//*[@id="editorWrapper"]/div[1]/div[2]/div/div/div/div').click()
        messageWriter = driver.find_element_by_xpath('//*[@id="editorWrapper"]/div[1]/div[2]/div/div/div/div').send_keys(MESSAGE)
        messageSender = driver.find_element_by_xpath('/html/body/div[7]/footer/div/div/div[2]/div[2]/button').click()
        messagePublisher = driver.find_element_by_xpath('/html/body/div[7]/footer/div/div/div[2]/div[2]/div/footer/div/button').click()
        time.sleep(3)

        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)


def flickrAutopost (USERNAME, PASSWORD, MESSAGE, driver):
    driver.get("https://identity.flickr.com/login?redir=https%3A%2F%2Fwww.flickr.com%2F")

    try:

        emailELement = driver.find_element_by_id("login-email").send_keys(USERNAME)
        emailSubmit = driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click()
        time.sleep(3)
        passwordElement = driver.find_element_by_id("login-password").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('//*[@id="login-form"]/button/span').click()
        time.sleep(3)

        driver.get("https://www.flickr.com/photos/upload/")
        time.sleep(5)

        photoChooser = WebDriverWait(browser, 10).until( EC.visibility_of_element_located((By.ID, 'button-add-photos'))).click()

        #BURADAN SONRASI ÇALIŞMIYOR

        currentUrl = driver.current_url
        with open('output.txt', 'a+') as f:
            f.write(currentUrl + "\n")


    except Exception as e:
        print(e)


def blogspotAutopost (USERNAME,PASSWORD,TITLE,MESSAGE,driver):
    driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.blogger.com%2Fhome&ltmpl=blogger&service=blogger&sacu=1&hl=tr&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    try:
        emailElement = driver.find_element_by_id("identifierId").send_keys(USERNAME)
        emailSubmit = driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        passwordElement = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(PASSWORD)
        passwordSubmit = driver.find_element_by_id("passwordNext").click()
        time.sleep(5)

        newPostButton = driver.find_element_by_xpath('//*[@id="blogger-app"]/div[3]/div[4]/div/div[1]/div[1]/a').click()
        time.sleep(3)
        titleWriter = driver.find_element_by_xpath('//*[@id="blogger-app"]/div[3]/div[3]/div/div/div/form/div[1]/input').send_keys(TITLE)
        messageWriter = driver.find_element_by_id("postingComposeBox").send_keys(MESSAGE)
        messageSender = driver.find_element_by_xpath('//*[@id="blogger-app"]/div[3]/div[3]/div/div/div/form/div[1]/span/button[1]').click()
        time.sleep(2)

    except Exception as e:
        print(e)


def pinterestAutopost (USERNAME, PASSWORD, TITLE, MESSAGE, driver):
    driver.get("https://tr.pinterest.com/login")

    try:
        emailElement = driver.find_element_by_id("email").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("password").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div[3]/div/div/div[3]/form/div[5]/button/div').click()
        time.sleep(3)

        profileElement = driver.find_element_by_xpath('//*[@id="HeaderContent"]/div/div/div/div[2]/div/div/div[3]/div[3]/div/div/div/div/div/a/div/div').click()
        time.sleep(3)
        addPost = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[1]/button/div').click()
        pinSelector = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div').click()
        time.sleep(3)


        #titleWriter = driver.find_element_by_class_name("TextArea__textArea TextArea__bold TextArea__light TextArea__enabled TextArea__large TextArea__wrap").click()
        #titleWriter.send_keys(TITLE)
        saveFromSite = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/button')
        saveFromSite.send_keys(Keys.END)
        saveFromSite.click()
        messageWriter = driver.find_element_by_id("pin-draft-website-link").send_keys(MESSAGE)

        photoSelector = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/div/div/div[2]/div').click()
        time.sleep(5)

        scrollUpElement = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[1]/button').send_keys(Keys.HOME)
        photoAdder = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div[1]/img').click()
        photoPinner = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/button').click()
        time.sleep(3)

        categorySelector = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[1]').click()
        time.sleep(3)
        selectedCategory = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/div/div/div').click()
        savePhoto = driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[3]/div/div/div/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div/div/div/button[2]').click()
        time.sleep(5)
        showNow = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a/button').click()
        time.sleep(3)

        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")


    except Exception as e:
        print(e)


def slashdotAutopost (USERNAME, PASSWORD, TITLE, MESSAGE,driver):
    driver.get("https://slashdot.org/my/login")

    try:
        #loginSelector = driver.find_element_by_xpath('/html/body/div[2]/div[1]/nav[2]/ul/li[1]/a').click()
        usernameElement = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/div[2]/div[1]/form/fieldset/div[1]/input').send_keys(USERNAME)
        passwordElement = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/div[2]/div[1]/form/fieldset/div[2]/input').send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/div[2]/div[1]/form/fieldset/input[3]').click()
        time.sleep(3)

        messageSelector = driver.find_element_by_xpath('/html/body/div[2]/div[1]/nav[1]/a').click()
        time.sleep(5)
        titleSelector = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/section/div/div/div[2]/form/p[1]/input').click()
        titleWriter = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/section/div/div/div[2]/form/p[1]/input').send_keys(MESSAGE)
        messageWriter = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/section/div/div/div[2]/form/p[2]/textarea').send_keys(MESSAGE)
        urlWriter = driver.find_element_by_xpath('/html/body/section[1]/div[3]/div/div/section/div/div/div[2]/form/p[4]/input').send_keys(MESSAGE)
        messagePreviewElement = driver.find_element_by_id("edit-preview-button").click()

        #BURADAN SONRA KONTROL ÇIKIYOR

    except Exception as e:
        print(e)


def weheartitAutopost (USERNAME, PASSWORD, TITLE, MESSAGE, driver):
    driver.get("https://weheartit.com/login")

    try:
        emailElement = driver.find_element_by_id("user_email_or_username").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("user_password_login").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('//*[@id="new_user"]/div[3]/input').click()
        time.sleep(3)

        postSelector = driver.find_element_by_xpath('//*[@id="navbar"]/div/div/div[4]/div/div[1]/a').click()
        messageSelector = driver.find_element_by_xpath('//*[@id="addimages"]/div/div[1]/div[3]/a/i').click()
        time.sleep(3)

        titleWriter = driver.find_element_by_xpath('//*[@id="upload-container"]/div[2]/div[1]/div/div[1]/input').send_keys(MESSAGE)
        urlSender = driver.find_element_by_xpath('//*[@id="upload-container"]/div[2]/div[1]/div/div[2]/div').click()
        time.sleep(5)
        photoSelector = driver.find_element_by_xpath('//*[@id="upload-container"]/div[2]/div[2]/li[1]/div[1]').click()
        time.sleep(3)
        photoSender = driver.find_element_by_xpath('//*[@id="create-entry-form"]/input[13]').click()
        time.sleep(5)

        currentUrl = driver.current_url
        with open('output.txt','a+') as f:
            f.write(currentUrl + "\n")

    except Exception as e:
        print(e)


def folkdAutopost (USERNAME, PASSWORD,MESSAGE, driver):
    driver.get("http://www.folkd.com/page/login.html")
    try:
        usernameElement = driver.find_element_by_id("username").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("password").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_id("submit_login").click()
        time.sleep(3)

        driver.get("http://www.folkd.com")
        messageSelector = driver.find_element_by_xpath('//*[@id="container"]/div[4]/span[1]/a').click()
        time.sleep(3)
        messageWriter = driver.find_element_by_id("url_page").send_keys(MESSAGE)
        messageSubmit = driver.find_element_by_xpath('//*[@id="submit_page"]/button').click()
        time.sleep(3)
        messageSender = driver.find_element_by_xpath('//*[@id="container"]/div[4]/form/p/input').click()


    except Exception as e:
        print(e)


def soupioAutopost (USERNAME,PASSWORD,MESSAGE,driver):
    driver.get("https://www.soup.io/login")

    try:
        time.sleep(3)
        usernameElement = driver.find_element_by_id("login").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("password").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('//*[@id="loginform"]/form/div/p[3]/input').click()
        time.sleep(3)

        mysoupPageSelector = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a').click()
        time.sleep(3)
        messageSelector = driver.find_element_by_id("btn-new").click()
        messagePanel = driver.find_element_by_xpath('//*[@id="admin-new"]/li[2]/a').click()
        time.sleep(3)
        messageWriter = driver.find_element_by_id("post_source").send_keys(MESSAGE)
        messageSender = driver.find_element_by_xpath('//*[@id="new_post"]/div[3]/input').click()
        time.sleep(3)

        contentLink = driver.find_element_by_xpath('/html/body/div[10]/div[1]/div/div/div/div/div[2]/div/div[2]/div[4]/div/div[3]/div[1]/div/div[1]/a')
        contentUrl = contentLink.get_attribute("href")
        time.sleep(2)

        with open('output.txt', 'a+') as f:
            f.write(contentUrl + "\n")


    except Exception as e:
        print(e)


def deliciousAutopost (USERNAME,PASSWORD,MESSAGE,driver):
    driver.get("https://del.icio.us/login")

    try:
        usernameElement = driver.find_element_by_xpath('//*[@id="user-login-form"]/div/input[1]').send_keys(USERNAME)
        passwordElement = driver.find_element_by_xpath('//*[@id="user-login-form"]/div/input[2]').send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('//*[@id="user-login-form"]/div/div/button').click()

        #ÜYELİK KAPALI OLDUĞU İÇİN SONRASI BİLİNMİYOR AÇILINCA YAP

    except Exception as e:
        print(e)


def redditAutopost (USERNAME,PASSWORD,TITLE,MESSAGE,driver):
    driver.get("https://www.reddit.com/login/")

    try:
        usernameElement = driver.find_element_by_id("loginUsername").send_keys(USERNAME)
        passwordElement = driver.find_element_by_id("loginPassword").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/form/fieldset[5]/button').click()
        time.sleep(7)

        linkSelector = driver.find_element_by_id("post-composer-du-link").click()
        time.sleep(5)

        categorySelector = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[1]/input').send_keys(USERNAME+Keys.ENTER)
        titleWriter = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[1]/div/textarea').send_keys(MESSAGE)
        messageWriter = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[2]/div[2]/textarea').send_keys(MESSAGE)
        time.sleep(5)

        messageSender = driver.find_element_by_xpath('//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[2]/div[3]/div[3]/div[2]/div/div[1]/button').click()
        time.sleep(5)


        currentUrl = driver.current_url
        with open('output.txt', 'a+') as f:
            f.write(currentUrl + "\n")


    except Exception as e:
        print(e)


def mediumAutopost (EMAIL, PASSWORD, TITLE, MESSAGE, driver):
    driver.get("https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F")

    try:
        time.sleep(3)
        emailSelector = driver.find_element_by_xpath('//*[@id="_obv.shell._surface_1584477934266"]/div/div[3]/div/section/div[1]/div/button[4]/span[1]').click()
        usernameElement = driver.find_element_by_id("email").send_keys(EMAIL)
        passwordElement = driver.find_element_by_id("pass").send_keys(PASSWORD)
        loginSubmit = driver.find_element_by_id("login_button").click()

    except Exception as e:
        print(e)

#browser.get("http://whatismyipaddress.com")


userCounter = input("Hesap sayısını gir: ")
message = input("Yazılacak mesajları gir: ")
title = input("Gereken yerler için başlık gir: ")

with open('input.json') as f:
    inputData = json.load(f)

for x in range(1,(int(userCounter)+1)):

    PROXY = "14.207.40.156:8213"

    option = Options()
    # option.add_argument('--proxy-server=%s' % PROXY)
    option.add_argument("user-agent=tarkan_batar")
    option.add_argument("--disable-web-security")
    option.add_argument("--allow-running-insecure-content")
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_argument("--enable-javascript")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    option.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile': {
            'password_manager_enabled': False
        }
    })
    browser = webdriver.Chrome(chrome_options=option, executable_path=r'/Users/tarkanbatar/Desktop/chromedriver')
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """
    })
    browser.execute_cdp_cmd("Network.enable", {})
    browser.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}})

    twitterUsername = inputData["twitter"]["USERNAME" + str(x)]
    twitterPassword = inputData["twitter"]["PASSWORD" + str(x)]
    twitterAutopost(twitterUsername,twitterPassword,message,browser)

    linkedinUsername = inputData["linkedin"]["USERNAME" + str(x)]
    linkedinPassword = inputData["linkedin"]["PASSWORD" + str(x)]
    linkedinAutopost(linkedinUsername,linkedinPassword,message,browser)

    plurkUsername = inputData["plurk"]["USERNAME" + str(x)]
    plurkPassword = inputData["plurk"]["PASSWORD" + str(x)]
    plurkAutopost(plurkUsername,plurkPassword,message,browser)

    tumblrUsername = inputData["tumblr"]["USERNAME" + str(x)]
    tumblrPassword = inputData["tumblr"]["PASSWORD" + str(x)]
    tumblrAutopost(tumblrUsername,tumblrPassword,message,browser)

    scoopitUsername = inputData["scoopit"]["USERNAME" + str(x)]
    scoopitPassword = inputData["scoopit"]["PASSWORD" + str(x)]
    scoopitAutopost(scoopitUsername,scoopitPassword,message,browser)

    instapaperUsername = inputData["instapaper"]["USERNAME" + str(x)]
    instapaperPassword = inputData["instapaper"]["PASSWORD" + str(x)]
    instapaperAutopost(instapaperUsername,instapaperPassword,message,browser)

    livejournalUsername = inputData["livejournal"]["USERNAME" + str(x)]
    livejournalPassword = inputData["livejournal"]["PASSWORD" + str(x)]
    livejournalAutopost(livejournalUsername,livejournalPassword,message,browser)

    soupioUsername = inputData["soupio"]["USERNAME" + str(x)]
    soupioPassword = inputData["soupio"]["PASSWORD" + str(x)]
    soupioAutopost(soupioUsername,soupioPassword,message,browser)

    weheartitUsername = inputData["weheartit"]["USERNAME" + str(x)]
    weheartitPassword = inputData["weheartit"]["PASSWORD" + str(x)]
    weheartitAutopost(weheartitUsername,weheartitPassword,message,browser)

    pinterestUsername = inputData["pinterest"]["USERNAME" + str(x)]
    pinterestPassword = inputData["pinterest"]["PASSWORD" + str(x)]
    pinterestAutopost(pinterestUsername,pinterestPassword,message,browser)

    redditUsername = inputData["reddit"]["USERNAME" + str(x)]
    redditPassword = inputData["reddit"]["PASSWORD" + str(x)]
    redditAutopost(redditUsername,redditPassword,message,browser)

    browser.close()

#twitterAutopost(USERNAME,PASSWORD,MESSAGE, browser)
#linkedinAutopost(EMAIL,PASSWORD2,MESSAGE, browser)
#plurkAutopost(PLURKUSERNAME,PLURKPASSWORD,MESSAGE,browser)
#tumblrAutopost(TUMBLRUSERNAME,TUMBLRPASSWORD,MESSAGE,browser)
#scoopitAutopost(SCOOPITEMAIL,SCOOPITPASSWORD,MESSAGE,browser)
#instapaperAutopost(INSTAPAPERUSERNAME,INSTAPAPERPASSWORD,MESSAGE,browser)
#livejournalAutopost(LIVEJOURNALUSERNAME,LIVEJOURNALPASSWORD,MESSAGE,browser)
#soupioAutopost(SOUPIOUSERNAME,SOUPIOPASSWORD,MESSAGE,browser)
#weheartitAutopost(FLICKREMAIL,SOUPIOPASSWORD,MESSAGE,MESSAGE,browser)
#pinterestAutopost(FLICKREMAIL, SOUPIOPASSWORD,TITLE, MESSAGE, browser)
#redditAutopost (SOUPIOUSERNAME, SOUPIOPASSWORD,TITLE,MESSAGE,browser)

#slashdotAutopost(SOUPIOUSERNAME,BLOGSPOTPASSWORD,TITLE,MESSAGE,browser) #En sonda resimli kontrol çıkıyor
#folkdAutopost(FOLKDUSERNAME,FOLKDPASSWORD,MESSAGE2,browser) # En sonunda recaptcha çıkıyor ona tıklatmayı dene -  denedim olmuyor
#mediumAutopost(FLICKREMAIL,BLOGSPOTPASSWORD,TITLE,MESSAGE,browser) #recaptcha
#blogspotAutopost(BLOGSPOTEMAIL,BLOGSPOTPASSWORD,TITLE,MESSAGE,browser) #Google tarayıcıya güvenmiyor
#flickrAutopost(FLICKREMAIL,FLICKRPASSWORD,MESSAGE,browser) # Upload butonuna tıklamıyor
