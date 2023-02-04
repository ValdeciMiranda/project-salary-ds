# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:43:02 2023

@author: Valde
"""

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd


def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    
    #Change the path to where chromedriver is in your home folder.
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)

    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    
    #url = "https://www.glassdoor.com/Job/"+keyword+"-jobs-SRCH_KO0,14_IP14.htm?includeNoSalaryJobs=true" #PAGE 14 LOADING ERROR
    
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0' #FIRST URL
    
    driver.get(url)
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.

        #Let the page load. Change this number based on your internet speed.
        #Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(slp_time)

        #Test for the "Sign Up" prompt and get rid of it.
        try:
            #driver.find_element_by_class_name("selected").click()
            #driver.find_elements(By.CLASS_NAME, 'react-job-listing css-wp148e eigr9kq4').click()
            newselected = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[1]")
            newselected.click() 
            
            """
            #This code apear to be out to date, this because the selection per CSS Class no longer works in this site, 
            #the dev team of Glassdoor reformulated the page and now exist the boolean indicator of selection data-selected="true", 
            #or "false" for not selected job. Also, the "find_element_by_class_name" apear to no longer exist in newer versions of selenium
            #Instead we have to use  driver.find_elements(By.CLASS, 'selected') to access the  tag li instead of access the class selected, for this
            #we have to import: from selenium.webdriver.common.by import By.
                                    
            Something unique that can be used to catch data from the jobs is the class, that is diferent to one job that were in blue color that means 
            selected and a job that were not selected are from another CSS class, in the actual version of this site the class "selected" don't even 
            exist in the CSS instead, to hi light the selected job it's used the css class="react-job-listing css-7x0jr eigr9kq4", 
            and to the not selected job it's used the class="react-job-listing css-wp148e eigr9kq4", because of this change on this site I had 
            to alter all the code.
            
            So, I tested the method above, but, does not work becouse it returns out a list that does not have an attribute click becouse of it I used
            XPath and it worked! So, the Xpath is the best solution to find this element and initiate the bot by clicking in it.
            """
            
        except ElementClickInterceptedException:
            pass

        time.sleep(.1)

        try:
            #driver.find_element_by_class_name("ModalStyle__xBtn___29PT9").click()  #clicking to the X. 
            #driver.find_elements(By.CLASS_NAME, 'SVGInline modal_closeIcon').click() #SVGInline-svg modal_closeIcon-svg
            #clickonthex = driver.find_element(By.XPATH, "/html/body/div[15]/div/div[2]/span/svg/path") #/html/body/div[15]/div/div[2]/span/svg/path
            #clickonthex.click() 
            """
            This also has to be modified becouse the method find_element_by_class_name is deprecated in newer versions of selenium 
            The piece of code bellow: driver.find_element_by_css_selector('[alt="Close"]').click(), worked for some reason, but the XPath not
            I does not know why, but worked.
            """
            driver.find_element_by_css_selector('[alt="Close"]').click() 
            
            """
            The closing X worked but for avoid the AFK error of the page, I guess that I need to login in an account for it, because of that, the piece
            of code following is to login in an account before start working.
            """

            """            
            try:
                emailbuttton = driver.find_element(By.CLASS_NAME, "jaCreateAccountEmailSignUpButton")
                emailbuttton.click() 
                
                emailinput = driver.find_element(By.XPATH, "//input[@type='email']")
                emailinput.click()
                emailinput.sendKeys("emersedcoder@gmail.com" + Keys.ENTER)
                
            except ElementClickInterceptedException:
                emailinput = driver.find_element(By.XPATH, "//input[@type='email']")
                emailinput.click()
                emailinput.sendKeys("emersedcoder@gmail.com" + Keys.ENTER)
            """
            
            #emailbuttton = driver.find_element(By.CLASS_NAME, "jaCreateAccountEmailSignUpButton")
            #emailbuttton.click() 

            #element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
            #driver.execute_script("scrollIntoView(); arguments[0].click();", element)

            #emailbuttton = driver.find_element(By.CLASS_NAME, "google gd-btn ")
            #emailbuttton.click()
                        
            #emailinput = driver.find_element(By.XPATH, "//input[@type='email']")
            #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='email']")))
            #emailinput = driver.find_element(By.TAG_NAME, "//input[@type='email']")
            
            #element = driver.find_element(By.CLASS_NAME, 'background-overlay')
            #driver.execute_script("""
            #var element = arguments[0];
            #element.parentNode.removeChild(element);
            #""", element)
            
            
            #clicktitle = driver.find_element(By.CLASS_NAME, "jaCreateAccountTitle mt-0")
            #clicktitle.click() 
            
            #emailbuttton = driver.find_element(By.CLASS_NAME, "jaCreateAccountEmailSignUpButton")
            #emailbuttton.click() 
            
            #element = driver.find_element_by_css_selector("input[placeholder='Enter email address']")
            #driver.execute_script("arguments[0].click();", element)

            """
            emailinput = driver.find_element(By.XPATH, "//input[@type='email']")
            emailinput.click()
            emailinput.sendKeys("emersedcoder@gmail.com" + Keys.ENTER)
            """
            
            print('x out of worked')
        except NoSuchElementException:
            print('x out filed')
            pass

        
        #Going through each job in this page
        #job_buttons = driver.find_elements_by_class_name("jl")  #jl for Job Listing. These are the buttons we're going to click.
        #job_buttons = driver.find_element(By.TAG_NAME,"li")
        #job_buttons = driver.find_element(By.CSS_SELECTOR, "data-selected")
        
        job_buttons = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li")
        
        """
        list = [str(x) for x in range(num_jobs)]
        
        job_buttons = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[".join(list) + "]")
        
        that code list above create a list auto increasing for xpath, but doesn't works because it repeats itself until all jobs are listed creating
        an loop. I guessed that detect the jobs buttons per tag name is better but not because the 'WebElement' object is not iterable. So, my last
        try I got from stackoverflow https://stackoverflow.com/questions/55080493/selenium-python-typeerror-webelement-object-is-not-iterable that
        I used correctly the find_element by changing the method to find_elements.
        
        
        This also has to be modified.
        """
        
        for job_button in job_buttons:  

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False
            
            while not collected_successfully:
                try:
                    
                    driver.implicitly_wait(1)
                    
                    """
                    company_name = driver.find_element_by_xpath('.//div[@class="employerName"]').text
                    location = driver.find_element_by_xpath('.//div[@class="location"]').text
                    job_title = driver.find_element_by_xpath('.//div[contains(@class, "title")]').text
                    job_description = driver.find_element_by_xpath('.//div[@class="jobDescriptionContent desc"]').text
                    
                    The code above is out to date, because of that, for the new version of glassdoor I had to change some acpects of it using an xpath
                    in every try and an except for every on it.
                    """
                    
                    """

                    The StaleElementReferenceException are added because of the StaleElementReferenceException: stale element reference: element is not attached to the page document

                    """
                    #id erro loading = JDCol
                    
                    company_name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                    print(company_name)

                    location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    print(location)
                        
                    job_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    print(job_title)

                    job_description = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]').text
                    print(job_description)                        
                        
        
                    collected_successfully = True
                    
                except NoSuchElementException:
                    
                    #if 
                    
                    print("We have an expetion here: NoSuchElementException")
                    
                    job_description = -1
                    print(job_description)
                    
                    job_title = -1
                    print(job_title)
                    
                    location = -1
                    print(location)
                    
                    company_name = -1
                    print(company_name)
                    
                except StaleElementReferenceException:
                    job_description = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]').text
                    print(company_name)
                    
                    job_title = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
                    print(company_name)
                    
                    location = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    print(company_name)
                    
                    company_name = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[1]/div').text
                    print(company_name)
                    
                    time.sleep(5)

            try:
                
                salary_estimate = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
                print(salary_estimate)
                
                """
                salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
                the method find_element_by_xpath is also deprecated.
                """
                
            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."
                print(salary_estimate)
            except StaleElementReferenceException:
                salary_estimate = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[4]/span').text
                print(salary_estimate)
            
            try:
                
                rating = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[28]/div[1]/span').text
                print(rating)
                
                """
                rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
                
                Also modify this.
                """
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."
                print(rating)
            except StaleElementReferenceException:
                rating = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[1]/ul/li[28]/div[1]/span').text
                print(rating)

            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))

            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            try:
                
                driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]').click()
                
                """
                driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
                This method find_element_by_xpath also  has to be modified.
                """

                try:
                    
                    #<div class="infoEntity">
                    #    <label>Headquarters</label>
                    #    <span class="value">San Francisco, CA</span>
                    #</div>
                    
                    #headquarters = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
                
                    headquarters = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text

                    print(headquarters)
                        
                except NoSuchElementException:
                    headquarters = -1
                    print(headquarters)
                except StaleElementReferenceException:
                    headquarters = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
                    print(headquarters)
                
                try:
                    #size = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
                    size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[1]').text
                    print(size)
                
                except NoSuchElementException:
                    size = -1
                    print(size)
                except StaleElementReferenceException:
                    size = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[1]').text
                    print(size)
                    
                try:
                    #founded = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
                    founded = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]').text
                    print(founded)
                
                except NoSuchElementException:
                    founded = -1
                    print(founded)
                except StaleElementReferenceException:
                    founded = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[2]/div/div/div[1]/div/div[2]').text
                    print(founded)
                    
                try:
                    #type_of_ownership = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
                    type_of_ownership = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[2]').text
                    print(type_of_ownership)
                
                except NoSuchElementException:
                    type_of_ownership = -1
                    print(type_of_ownership)
                except StaleElementReferenceException:
                    type_of_ownership = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[2]').text
                    print(founded)
                    
                try:
                    #industry = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
                    industry = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[3]').text
                    print(industry)
                
                except NoSuchElementException:
                    industry = -1
                    print(industry)
                except StaleElementReferenceException:
                    industry = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[3]').text
                    print(industry)
 
                try:
                    #sector = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
                    sector = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[4]').text
                    print(sector)
 
                except NoSuchElementException:
                    sector = -1
                    print(sector)
                except StaleElementReferenceException:
                    sector = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[4]').text
                    print(sector)
 
                try:
                    #revenue = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
                    revenue = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[5]').text
                    print(revenue)
 
                except NoSuchElementException:
                    revenue = -1
                    print(revenue)
                except StaleElementReferenceException:
                    revenue = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[3]/div/div/div[1]/div/div[5]').text
                    print(revenue)
     
                """
                try:
                    #competitors = driver.find_element_by_xpath('.//div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
                    competitors = driver.find_element(By.XPATH, '').text
                except NoSuchElementException:
                    competitors = -1
                    
                    
                    This all above as to be modifed becouse of the find_element_by_xpath method.
                    """

            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                #competitors = -1
            except StaleElementReferenceException:
                headquarters = -1
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1
                #competitors = -1

                
            if verbose:
                print("Headquarters: {}".format(headquarters))
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                #print("Competitors: {}".format(competitors))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Headquarters" : headquarters,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue,
            #"Competitors" : competitors})
            #add job to jobs
            })
        #Clicking on the "next page" button
        try:
            #driver.find_element_by_xpath('.//li[@class="next"]//a').click()
            driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/section/article/div[2]/div/div[1]/button[7]').click()
            currenturl = driver.current_url
            driver.implicitly_wait(1)
            print("THE CURRENT URL IS: ", currenturl)
            driver.implicitly_wait(1)

            """
            This also as to be modified.
            """
        except NoSuchElementException:
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
            break

    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.

