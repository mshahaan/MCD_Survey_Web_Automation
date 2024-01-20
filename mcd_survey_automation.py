from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint


# DEBUG CODE AND SET BREAKPOINT ON FINAL LINE OF automated_survey FUNC IN
# ORDER TO PREVENT BROWSER CLOSE UPON SCRIPT HAS COMPLETED EXECUTION



# TODO : COMMENT CODE HEAVILY

def automated_survey(code_segments):
    
    # TAKES IN A LIST code_segments AS AN ARG WHICH IS ASSUMED TO HAVE SIX
    # INDECES CONTAINING A SIX-PART SURVEY CODE. IT IS ALSO ASSUMED THE 
    # FORMATTING OF THE LIST IS CORRECT BUT IT IS NOT ASSUMED THAT THE CODE
    # IS VALID

    # INITIALIZATION OF WEB BROWSER
    browser = webdriver.Chrome()

    ###################### INITIAL TEST CODE ##########################

    # CODE TO TEST IF WEB AUTOMATION IS WORKING
    # OBSOLETE

    #browser.get("https://www.google.com/")
    #
    #text_box = browser.find_element(By.CLASS_NAME, "gLFyf")
    #
    #text_box.send_keys("black cat" + Keys.ENTER)

    ###################### END TEST CODE ##############################

    #Redirecting Browser to McDonald's Survey Entry Site
    browser.get("https://www.mcdvoice.com/?AspxAutoDetectCookieSupport=1")


    ##################### ENTERING SURVEY CODE ########################

    # THE SURVERY CODE IS MADE UP OF 5 FIVE DIGIT CODES AND 1 ONE DIGIT CODE
    # FOR A TOTAL OF ONE 26 DIGIT CODE

    # EACH SEGMENT IS ENTERED IN ITS OWN TEXTBOX OF WHICH THERE ARE SIX, EACH
    # WITH ELEMENT ID CNx FOR THE xth TEXTBOX

    # TEXTBOX ONE WHICH ACCEPTS THE FIRST FIVE DIGIT CODE
    # THIS CODE IS THE FIVE DIGIT STORE NUMBER OF THE RESTAURANT
    code_entry_box_1 = browser.find_element(By.ID, "CN1")
    code_entry_box_1.send_keys(code_segments[0])

    # TEXTBOX TWO WHICH ACCEPTS THE SECOND FIVE DIGIT CODE
    code_entry_box_2 = browser.find_element(By.ID, "CN2")
    code_entry_box_2.send_keys(code_segments[1])

    # TEXTBOX THREE WHICH ACCEPTS THE THIRD FIVE DIGIT CODE
    code_entry_box_3 = browser.find_element(By.ID, "CN3")
    code_entry_box_3.send_keys(code_segments[2])

    # TEXTBOX FOUR WHICH ACCEPTS THE FOURTH FIVE DIGIT CODE
    code_entry_box_4 = browser.find_element(By.ID, "CN4")
    code_entry_box_4.send_keys(code_segments[3])

    # TEXTBOX FIVE WHICH ACCEPTS THE FIFTH FIVE DIGIT CODE
    code_entry_box_5 = browser.find_element(By.ID, "CN5")
    code_entry_box_5.send_keys(code_segments[4])

    # TEXTBOX SIX WHICH ACCEPTS THE FINAL SINGLE DIGIT OF THE SURVEY CODE
    # THE ENTER KEY IS ALSO ENTERED HERE TO SUBMIT THE FORM AND ENTER THE SURVEY
    code_entry_box_6 = browser.find_element(By.ID, "CN6")
    code_entry_box_6.send_keys(code_segments[5] + Keys.ENTER)

    ####################################################################

    # TODO : COMMENT CODE IN REMAINING PORTION OF FUNC BELOW

    try:
        assert "Upon completion of this survey you will be given a validation code that can be used to redeem the offer printed on your receipt." in browser.page_source
    except AssertionError:
        print("Invalid Code")
        return

    if code_segments[1][0:2] == "01" or code_segments[1][0:2] == "02" or code_segments[1][0:2] == "13" or code_segments[1][0:2] == "15":
        #FRONTLINE ORDER
        browser.find_element(By.ID, "textR000455.1").click()
        browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    elif code_segments[1][0:2] == "06" or code_segments[1][0:2] == "07":
        #KIOSK ORDER
        browser.find_element(By.ID, "textR000455.2").click()
        browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    else:
        print("Invalid Code")
        return

    if code_segments[1][0] == "0":
        #CARRY-OUT OR DINE-IN ORDER
        browser.find_element(By.ID, "textR004000.3").click()
        browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    elif code_segments[1][0] == "1":
        #DRIVE-THRU ORDER
        browser.find_element(By.ID, "textR004000.2").click()
        browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()
    else:
        print("Invalid Code")
        return

    browser.find_element(By.XPATH, '//*[@id="FNSR001000"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR000444"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR000473"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR000474"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    question_codes = {
        'The speed of service.' : '008000',
        'The cleanliness of the restaurant.' : '000351',
        'The quality of your food.' : '028000',
        'The ease of placing your order' : '011000',
        'The friendliness of the employees.' : '009000',
        'The taste of your food.' : '005000',
        'The accuracy of your order.' : '007000',
        'The temperature of your food.' : '006000',
        'The overall value for the price you paid.' : '015000',
    }

    for prompt in question_codes:
        if prompt in browser.page_source:
            browser.find_element(By.XPATH, '//*[@id="FNSR' + question_codes[prompt] + '"]/td[1]/label').click()

    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    for prompt in question_codes:
        if prompt in browser.page_source:
            browser.find_element(By.XPATH, '//*[@id="FNSR' + question_codes[prompt] + '"]/td[1]/label').click()

    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="textR000373"]').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR016000"]/td[2]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR019000"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="FNSR018000"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.ID, "S081000").send_keys("Automated message from Shawn." + Keys.ENTER + Keys.ENTER + 
        "Auto-Generated message indicating auto-completion of survey with the following code :" + Keys.ENTER + Keys.ENTER +
        code_segments[0] + "-" + code_segments[1] + "-" + code_segments[2] + "-" + code_segments[4] + "-" +
        code_segments[5])
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    if "Were you asked to pull forward out of the drive-thru lane to wait for your order? " in browser.page_source:
        browser.find_element(By.XPATH, '//*[@id="FNSR000026"]/td[2]/label').click()
        browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.ID, "textR020000." + str(randint(1,4))).click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="textR000387.4"]').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="FNSR000482"]/td[1]/label').click()
    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()

    browser.find_element(By.XPATH, '//*[@id="NextButton"]').click()


    #RANDOM CODE FOR DEBUGGER
    #SET BREAKPOINT HERE TO STOP BROWSER FROM CLOSING UPON PROGRAM COMPLETION
    rand_var = 3

    browser.close()

#####################################################################################



################## MAIN SCRIPT ########################

# TODO : CREATE LOOP THAT STARTS FROM CURRENT DATE / TIME AND PROCEDURALLY GENERATES 
#        26 DIGIT CODES AND PLACES EACH INTO A LIST OF 6 ELEMENTS FORMATTED AS IS ON
#        THE MCDONALDS SURVEY SITE AND CALLS THE automated_survey FUNCTION USING EACH
#        GENERATED LIST

# CURRENT FUNCTIONALITY

# LIST STORING SIX-PART SURVEY CODE VALUE
list = ["22975", "02170", "41823", "14160", "00027", "4"]
automated_survey(list)
list = ["22975", "02180", "41823", "14192", "00112", "9"]
automated_survey(list)
list = ["22975", "02130", "41823", "13583", "00075", "5"]
automated_survey(list)
list = ["22975", "02140", "41823", "14035", "00026", "4"]
automated_survey(list)
list = ["22975", "02160", "41823", "14147", "00170", "3"]

# PASSING LIST INTO automated_survey FUNCTION
automated_survey(list)

