from selenium import webdriver
from selenium.webdriver.firefox import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import csv
import string
from time import sleep
import random
import time
import os
import pandas as pd
from random import randint

def human_clicker_js(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath)))
    driver_arg.execute_script("arguments[0].click();", element)

def human_clicker_click(driver_arg, xpath):
    element = WebDriverWait(driver_arg, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath)))
    element.click()
def human_typer(driver_arg, xpath, text: str):
    element = WebDriverWait(driver_arg, 10).until(
    EC.presence_of_element_located((By.XPATH, xpath)))

chrome_options= webdriver.ChromeOptions()  
chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver= webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
driver.get('https://www.google.com')
print(driver.page_source)    
# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options)
# driver.get('https://www.rapidcarcheck.co.uk/')
driver.maximize_window()
def carDetails():
    import pygsheets
    count=1
    gc = pygsheets.authorize(service_file='main-project-366913.json')
    sh = gc.open('New Sheet')
    wks = sh[1] # select the first sheet
    read = wks.get_as_df()
    cars = wks.get_all_records()

    for car in range (0,len(cars)):
        count=count+1
        reg=cars[car]['registration']
#         print(reg)
        make = cars[car]['make']
#         print(make)
        if not make:
            print("yess")
            sleep(randint(4,6))
            try:
                regNo = driver.find_element(By.XPATH,"//input[@name='RegPlate']").clear()
            except:
                ()
#             print("Enter Your Registration Number:")
            
            regNo = driver.find_element(By.XPATH,"//input[@name='RegPlate']").send_keys(reg)

            human_clicker_js(driver, "//button[@id='btnPost1']")
            sleep(randint(2,4))
            try:
                registration= driver.find_element(By.XPATH,"//div/p[contains(text(),'Reg')]/strong").text
                print(registration)
            except:
                registration = "None"

            try:
                make = driver.find_element(By.XPATH,"//div/p[contains(text(),'Make')]/strong").text
                print(make)
            except:
                make = "None"

            try:
                Model= driver.find_element(By.XPATH,"//div/p[contains(text(),'Model')]/strong").text
                print(Model)
            except:
                Model = "None"
            try:  
                Colour= driver.find_element(By.XPATH,"//div/p[contains(text(),'Colour')]/strong").text
                print(Colour)
            except:
                Colour = "None"

            try:
                VehicleType= driver.find_element(By.XPATH,"//div/p[contains(text(),'Vehicle Type')]/strong").text
                print(VehicleType)
            except:
                VehicleType = "None"

            try:
                BodyStyle= driver.find_element(By.XPATH,"//div/p[contains(text(),'Body Style')]/strong").text
                print(BodyStyle)
            except:
                BodyStyle = "None"
            try:
                FuelType= driver.find_element(By.XPATH,"//div/p[contains(text(),'Fuel Type')]/strong").text
                print(FuelType)
            except:
                FuelType = "None"
            try:
                EngineSize= driver.find_element(By.XPATH,"//div/p[contains(text(),'Engine Size')]/strong").text
                print(EngineSize)
            except:
                 EngineSize="None"
            try:
                BHP= driver.find_element(By.XPATH,"//div/p[contains(text(),'BHP')]/strong").text
                print(BHP)
            except:
                BHP="None"
            try:
                TopSpeed= driver.find_element(By.XPATH,"//div/p[contains(text(),'Top Speed')]/strong").text
                print(TopSpeed)
            except:
                TopSpeed = "None"
            try:
                MPH= driver.find_element(By.XPATH,"//div/p[contains(text(),'MPH')]/strong").text
                print(MPH)
            except:
                MPH = "None"
            try:
                AVGYearlyMileage= driver.find_element(By.XPATH,"//div/p[contains(text(),'AVG Yearly Mileage')]/strong").text
                print(AVGYearlyMileage)
            except:
                AVGYearlyMileage = "None"
            try:
                V5CIssueDate= driver.find_element(By.XPATH,"//div/p[contains(text(),'V5C Issue Date')]/strong").text
                print(V5CIssueDate)
            except:
                V5CIssueDate = "None"
            try:
                VehicleAge = driver.find_element(By.XPATH,"//div/p[contains(text(),'Vehicle Age')]/strong").text
                print(VehicleAge)
            except:
                VehicleAge = "None"
            try:
                Year= driver.find_element(By.XPATH,"//div/p[contains(text(),'Year')]/strong").text
                print(Year)
            except:
                Year = "None"
            try:
                TAXDueDate= driver.find_element(By.XPATH,"//div/p[contains(text(),'TAX Due Date')]/strong").text
                print(TAXDueDate)
            except:
                TAXDueDate = "None"
            try:
                DaysLeft= driver.find_element(By.XPATH,"//div/p[contains(text(),'Days Left')]/strong").text
                print(DaysLeft)
            except:
                DaysLeft = "None"
            try:
                Emissions= driver.find_element(By.XPATH,"//div/p[contains(text(),'Emissions')]/strong").text
                print(Emissions)
            except:
                Emissions = "None"
            try:
                LastRecord= driver.find_element(By.XPATH,"//div/p[contains(text(),'Last Record')]/strong").text
                print(LastRecord)
            except:
                LastRecord = "None"
            try:
                EstimatedTotalMileage= driver.find_element(By.XPATH,"//div/p[contains(text(),'Estimated Total Mileage')]/strong").text
                print(EstimatedTotalMileage)
            except:
                EstimatedTotalMileage = "None"
            try:
                Urban= driver.find_element(By.XPATH,"//div/p[contains(text(),'Urban')]/strong").text
                print(Urban)
            except:
                Urban ="None"
            try:
                ExtraUrban= driver.find_element(By.XPATH,"//div/p[contains(text(),'Extra-Urban')]/strong").text
                print(ExtraUrban)
            except:
                ExtraUrban = "None"
            try:
                Combined= driver.find_element(By.XPATH,"//div/p[contains(text(),'Combined')]/strong").text
                print(Combined)
            except:
                Combined ="None"
            try:
                perMileFuelCost= driver.find_element(By.XPATH,"//div/p[contains(text(),'1 Mile Fuel Cost')]/strong").text
                print(perMileFuelCost)
            except:
                perMileFuelCost = "None"
            

            sleep(3)
            temp_dict={}
            temp_list=[]
#             temp_dict['registration']= registration
            temp_dict['make']= make
            temp_dict['Model']= Model
            temp_dict['Name']= " "
            temp_dict['Price']= " "
            temp_dict['Cost']= " "
            temp_dict['Year']= " "
            temp_dict['Transmission']= " "
            temp_dict['Doors']= " "
            temp_dict['Seats']= " "
            temp_dict['Trim']= " "
            temp_dict['VIN']= " "
            temp_dict['Status']= ""
            temp_dict['Category']= "Vehicle"
            temp_dict['Colour']= Colour
            temp_dict['VehicleType']= VehicleType
            temp_dict['BodyStyle']= BodyStyle
            temp_dict['FuelType']= FuelType
            temp_dict['EngineSize']= EngineSize
            temp_dict['BHP']= BHP
            temp_dict['TopSpeed']= TopSpeed
            temp_dict['AVGYearlyMileage']= AVGYearlyMileage
            temp_dict['TAXDueDate']= TAXDueDate
            temp_dict['DaysLeft']= DaysLeft
            temp_dict['Emissions']= Emissions
            temp_dict['LastRecord']= LastRecord
            temp_dict['EstimatedTotalMileage']= EstimatedTotalMileage
            temp_dict['Combined']= Combined
            temp_dict['perMileFuelCost']= perMileFuelCost
            temp_dict['READY TO POST']= " "
            temp_dict['V5CIssueDate']= V5CIssueDate
            temp_dict['VehicleAge']= VehicleAge
            temp_dict['YEAR']= Year
            temp_dict['Urban']= Urban
            temp_dict['ExtraUrban']= ExtraUrban
            temp_dict['MPH']= MPH

            temp_list.append(temp_dict)
            temp_dict={}
            
#     import pygsheets
#     gc = pygsheets.authorize(service_file='carsdata-366712-a50663fcd58e.json')
#     sh = gc.open('test1')

    #ROW SELECTION WHERE WE WANT TO UPDATE THE DATA
            update_row = count
            for t in temp_list:
                    wks = sh[1] 

                    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
                    last_row = len(cells)
                    values = t.values()
                    values_list = list(values)
                    wks.update_row(update_row, values=[values_list], col_offset = 1)
                    update_row = update_row +1
            driver.get('https://www.rapidcarcheck.co.uk/')
            sleep(3)
        else:
            print('data present')
    sleep(3)
    driver.get('https://www.rapidcarcheck.co.uk/')
    print('Wait for 10 minutes now.')
    sleep(10)
    data_input()
    sleep(400)
    

def data_input():
    import pygsheets
    import requests
    import json
    gc = pygsheets.authorize(service_file='main-project-366913.json')
    sh = gc.open('New Sheet')
    wks = sh[1] # select the first sheet
    cars = wks.get_all_records()
    for car in range (0,len(cars)):
        READYTOPOST=(cars[car]['READY TO POST']).lower()
        # print(READYTOPOST)
        if READYTOPOST== 'yes':
            print('YES')
            Name=cars[car]['Name']
#             print(Name)
            Status=cars[car]['Status']
#             print(Status)
            Seats=cars[car]['Seats']
#             print(Seats)
            Emissions=cars[car]['Emissions']
#             print(Emissions)
            Trim=cars[car]['Trim']
#             print(Trim)
            EngineSize=cars[car]['EngineSize']
#             print(EngineSize)
            AVGYearlyMileage=cars[car]['AVGYearlyMileage']
#             print(AVGYearlyMileage)
            Year=cars[car]['Year']
#             print(Year)
            Combined=cars[car]['Combined']
#             print(Combined)
            EstimatedTotalMileage=cars[car]['EstimatedTotalMileage']
#             print(EstimatedTotalMileage)
            LastRecord=cars[car]['LastRecord']
#             print(LastRecord)
            #####cf vehicle type
            BodyStyle=cars[car]['BodyStyle']
#             print(BodyStyle)
            Model=cars[car]['Model']
#             print(Model)
            registration=cars[car]['registration']
#             print(registration)
            perMileFuelCost=cars[car]['perMileFuelCost']
#             print(perMileFuelCost)
            FuelType=cars[car]['FuelType']
#             print(FuelType)
            Doors=cars[car]['Doors']
#             print(Doors)
            BHP=cars[car]['BHP']
#             print(BHP)
            make=cars[car]['make']
#             print(make)
            VIN=cars[car]['VIN']
#             print(VIN)
            TopSpeed=cars[car]['TopSpeed']
#             print(TopSpeed)
            Colour=cars[car]['Colour']
#             print(Colour)
            Category=cars[car]['Category']
#             print(Category)
            Transmission=cars[car]['Transmission']
#             print(Transmission)
            Cost=cars[car]['Cost']
#             print(Cost)
            Price=cars[car]['Price']
#             print(Price)
            Available=cars[car]['Status']
#             print(Available)

            urll = 'https://halalcars.myfreshworks.com/crm/sales/api/cpq/products'
            data={
                "product": {
                    "name": Name,
                    "custom_field": {
                        "cf_status": Status,
                        "cf_seats": Seats,
                        "cf_emissions": Emissions,
                        "cf_trim": Trim,
                        "cf_engine_size_cc": EngineSize,
                        "cf_avg_yearly_milage": AVGYearlyMileage,
                        "cf_year": Year,
                        "cf_combined_mpg": Combined,
                        "cf_odometer": EstimatedTotalMileage,
                        "cf_last_recorded_mileage": LastRecord,
                        "cf_vehicle_type": BodyStyle,
                        "cf_model": Model,
                        "cf_vehicle_reg": registration,
                        "cf_fuel_cost_per_mile": perMileFuelCost,
                        "cf_fuel_type": FuelType,
                        "cf_doors": Doors,
                        "cf_bhp": BHP,
                        "cf_make": make,
                        "cf_vin": VIN,
                        "cf_top_speed": TopSpeed,
                        "category": Category,
                        "cf_colour": Colour,
                        "cf_transmission": Transmission,
                        "cf_vehicle_cost": Cost,
                        "cf_vehicle_selling_price": Price

                    }
                }
            }
            headers = {'Authorization': 'Token token=zc49UdVMx8D9Y1m3gDkIAA','Content-Type': 'application/json'}
            r=requests.post(urll, data=json.dumps(data), headers=headers)
            print(r.status_code)

        else:
            ()
    print('data input done now wait 10 minutes.')
    print('\n\nProcess is going to be start again.')
    sleep(20)
    carDetails()
    sleep(300)
        


carDetails()
# data_input()
