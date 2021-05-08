from selenium import webdriver
import os, time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import sys
from faker import Faker 
from colorama import Fore, Back, Style
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
colorama.init()


# config
chrome_options = Options()
# change the directory to your chrome driver. for more instructions read the readme file.os
PATH = ('C:\\Program Files (x86)\\Chrome\\Application\\chromedriver.exe') 
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-data-dir=C:\\Users\\gabri\\Local\\Google\\Chrome\\")

driver = webdriver.Chrome(PATH)



def main4(argv):
	lesson = input('Enter lesson link for algerba')
	while True:
		driver.get(lesson)
		time.sleep(4)
		driver.refresh()
		time.sleep(4)
		q1 = driver.find_element_by_class_name('yui3-practiceagent-content')
		q2 = q1.text
		print(repr(q2))
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[1]/div/div[2]/button').click()
		time.sleep(4)
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[2]').click()
		time.sleep(4)
		#change this
		answer = driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[4]/div[2]/div/div/div[2]')
		ans = answer.text
		print(ans)
		driver.delete_all_cookies()
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[1]/div[2]/button').click()


def main1(argv):
	lesson = input('Enter an 8th grade lesson link')
	while True:
		driver.get(lesson)
		time.sleep(4)
		driver.refresh()
		time.sleep(4)
		q1 = driver.find_element_by_class_name('yui3-practiceagent-content')
		q2 = q1.text
		print(repr(q2))
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[1]/div/div[2]/button').click()
		time.sleep(4)
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[2]').click()
		time.sleep(4)
		#change this
		answer = driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[4]/div[2]/div/div/div/div/div[9]')
		ans = answer.text
		print(ans)
		driver.delete_all_cookies()
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[1]/div[2]/button').click()



def main2(argv):
	lesson = input('Please Enter A 7th Grade Lesson Link: ')
	while True:
		driver.get(lesson)
		time.sleep(4)
		driver.refresh()
		time.sleep(4)
		q1 = driver.find_element_by_class_name('yui3-practiceagent-content')
		q2 = q1.text
		print(repr(q2))
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[1]/div/div[2]/button').click()
		time.sleep(4)
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[2]').click()
		time.sleep(4)
		answer = driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[4]/div[2]/div/div/div/div/div')
		ans = answer.text
		print(ans)
		driver.delete_all_cookies()
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[1]/div[2]/button').click()
# 6th Grade
def main3(argv):
	lesson = input('Please Enter A 6th Grade Lesson Link: ')
	while True:
		driver.get(lesson)
		time.sleep(4)
		driver.refresh()
		time.sleep(4)
		q1 = driver.find_element_by_class_name('yui3-practiceagent-content')
		q2 = q1.text
		print(repr(q2))
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[1]/div/div[2]/button').click()
		time.sleep(4)
		driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/button[2]').click()
		time.sleep(4)
		answer = driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[4]/div[2]/div/div/div/div')
		ans = answer.text
		print(ans)
		driver.delete_all_cookies()
		driver.find_element_by_xpath('/html/body/div[9]/section/div[1]/div[1]/div[6]/div/div[8]/div/div[1]/div[1]/div[2]/button').click()




def op1():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('If any of these are incorrect, bot will fail.')
    username = input('Enter Username or Email: ')
    password = input('Enter Password:  ')
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
    print('do not touch the window that has just popped up. ')
    print('smart score goes up and down alot, just go afk or do something in background!')
    driver.get('https://www.ixl.com/math/grade-7/add-and-subtract-integers')
    time.sleep(3)
    driver.refresh()
    driver.find_element_by_xpath('//*[@id="qlusername"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="qlpassword"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="qlsubmit"]').click()
    driver.execute_script('''window.open('',"_blank");''')
    driver.switch_to.window(driver.window_handles[-1])
    driver.get('https://www.meta-calculator.com/scientific-calculator.php?panel-203-simple-calculator')
    driver.switch_to.window(driver.window_handles[0])

    while True:
        time.sleep(3)
        variable = driver.find_element_by_class_name('old-space-indent').text
        print(variable)
        driver.switch_to.window(driver.window_handles[-1])
        box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/input')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/input').send_keys(variable)
        
        answer = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/input')
        box.send_keys(Keys.BACKSPACE)
        print('the bot will now pause for 150 seconds to generate some time.')
        time.sleep(150)
        box.send_keys(Keys.ENTER)
        answer = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[1]/span[2]').text
        a = (answer)
        c = "="

        for char in c:
            a = a.replace(char, "")
        
        print(a)
        driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/button[2]').click()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_class_name('fillIn').click()
        driver.find_element_by_class_name('fillIn').send_keys(a)
        time.sleep(3)
        driver.find_element_by_class_name('fillIn').send_keys(Keys.ENTER)
        driver.refresh()

        
               

def op2():
    os.system('cls' if os.name == 'nt' else 'clear')
    grade = input('Are you in 8th Grade? (Y/N): ')
    if grade == "Y":
        main1(sys.argv)
        print('You are In 8th Grade')
        print('You will be asked to Enter Your Lesson Link')
    else:
        grade2 = input('Are you in 7th Grade? (Y/N): ')
        if grade2 == "Y":
            main2(sys.argv)
            print('You are In 7th Grade')
            print('You will be asked to Enter Your Lesson Link')

        else:
            grade3 = input('Are you in 6th Grade? (Y/N): ')
        if grade3 == "Y":
            print('You are In 6th Grade')
            print('You will be asked to Enter Your Lesson Link')
            main3(sys.argv)
        else:
            print('algerba')
            main4(sys.argv)



def op3():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.MAGENTA + """\
██╗██╗  ██╗██╗         ████████╗███████╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ██████╗  ██████╗ ████████╗
██║╚██╗██╔╝██║         ╚══██╔══╝██╔════╝██╔══██╗██╔════╝██║  ██║██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██║ ╚███╔╝ ██║            ██║   █████╗  ███████║██║     ███████║█████╗  ██████╔╝    ██████╔╝██║   ██║   ██║   
██║ ██╔██╗ ██║            ██║   ██╔══╝  ██╔══██║██║     ██╔══██║██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║   ██║   
██║██╔╝ ██╗███████╗       ██║   ███████╗██║  ██║╚██████╗██║  ██║███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
╚═╝╚═╝  ╚═╝╚══════╝       ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   """ + Style.RESET_ALL + Style.BRIGHT)

    print(Fore.RED + "                            w3lcs: https://instagram.com/w3lcs"+ Style.RESET_ALL + Style.BRIGHT)

    print(Fore.GREEN+ "[ OK ] ", end =""+ Style.RESET_ALL + Style.BRIGHT),
    print("Loaded Modules")
                                                                                                                
    print(Fore.RED+ "[ NOTE ] ", end =""+ Style.RESET_ALL + Style.BRIGHT),
    print("Code Will Loop Untill Bot Is Closed, Close Bot When You Get Your Desired Amount Of Accounts.")
    print(Fore.RED+ "[ NOTE ] ", end =""+ Style.RESET_ALL + Style.BRIGHT),
    print("Please Wait..")

    f = Faker()

    driver.get('https://www.ixl.com/membership/teachers/trial')


    # Your Information

    while True:
        driver.find_element_by_xpath('/html/body/main/form/section[2]/div[1]/input').send_keys(f.name())
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(1)
        driver.get("https://snapchat.tf/")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]').click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/main/form/section[2]/div[2]/input').send_keys(Keys.CONTROL, 'v')


        # Your School
        driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[1]/input').send_keys('90011')
        time.sleep(2)
        driver.find_element_by_class_name('select-institutionId').click()
        driver.find_element_by_xpath('/html/body/main/form/section[3]/div/div[2]/div[2]/div/select/optgroup[1]/option[1]').click()


        # IXL Quantity Selection
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys(f.word())
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys(f.word())
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[1]/input').send_keys(f.word())
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[2]/label').click()
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[1]/label').click()
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[3]/label').click()
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[2]/div[4]/label').click()
        driver.find_element_by_xpath('/html/body/main/form/section[4]/div[6]/div/button').click()
        time.sleep(2)

        # Printing Information For User
        driver.switch_to.window(driver.window_handles[1])
        driver.refresh()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        driver.refresh()
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        driver.refresh()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[1]/div/div').click()
        time.sleep(2)


        username = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[3]/div/div/div[5]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td')

        username2 = username.text
        print(Fore.RED+ "[ SUCCESS ] ", end =""+ Style.RESET_ALL + Style.BRIGHT),
        print(username2)
        password = driver.find_element_by_xpath('/html/body/main/div[1]/div/div[3]/div/div/div[5]/table/tbody/tr/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[3]/td')
        password2 = password.text
        print(Fore.RED+ "[ SUCCESS ] ", end =""+ Style.RESET_ALL + Style.BRIGHT),
        print(password2)
        driver.delete_all_cookies()
        driver.close();
        driver.switch_to.window(driver.window_handles[0])
        driver.get('https://www.ixl.com/membership/teachers/trial')



def op4():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('This is not done yet. Please watch for updates either on reddit or github.')

    

def op5():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Coded by @w3lcs')
    print('MY OTHER SOCIALS ARE')
    print('@debaet , REDDIT U/Q3LCS')
    print('MY GITHUB IS @DEBAET')
    

    

def main():
    print('Menu: ')
    print('1. Add more time to your account')
    print('2. Scrape Answers (get answers)')
    print('3. Get Teacher Accounts')
    print('4. Auto Answer (some lessons work)')
    print('5. Credits')
    var = input('Enter an Option: ')

    # goes to the specified option 
    if var==('1'):
        op1()

    elif var==('2'):
        op2()

    elif var==('3'):
        op3()
    elif var==('4'):
        op4()

    elif var==('5'):
        op5()

    else:
        print('Please enter numbers only. If you did and still got an error, please enter a number which is listed above.')
        time.sleep(4)
        os.system('cls' if os.name == 'nt' else 'clear')
        main()



# end code

print('Welcome to The First Functional IXL BOT.')
print('DO NOT CLOSE THE CHROME WINDOW THAT IS ABOUT TO POP UP.')
print('Please wait..')

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
main()

