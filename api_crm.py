def crm_Data():

    import base64
    import pygsheets
    import requests
    import json
    from time import sleep
    method = "get"
    apiKey="ck_eafcf2c7e7ea7bf332fb3d414c89eecc325c9ecb"
    secret="cs_4b6b304fc1be08673ce0664e950865c5fa7b6d60"
    auth_string = f"{apiKey}:{secret}"
    auth_string = auth_string.encode("ascii")
    auth_string = base64.b64encode(auth_string)
    headers = {
           'Accept': 'application/json',
           'Authorization' : f"Basic {auth_string.decode('ascii')}"
    }
    gc = pygsheets.authorize(service_file='main-project-366913.json')
    sh = gc.open('New Sheet')
    wks = sh[0] # select the first sheet
    read = wks.get_as_df()
    cars = wks.get_all_records()
    count = 0
    d=wks.cell((2,3)).value #sheet latest value

    pg=1
    val=500
    update_row = 2
    for x in range(0,1):
    # while True:    

        urll = "https://halalcars.co.uk/wp-json/gf/v2/entries/?paging[page_size]="+str(val)+"&paging[offset]="+str(pg)+"&"
        url=urll
        response = requests.request(method, url, headers=headers, auth=None)
        response_dict = json.loads(response.text)
        rsp=response_dict['entries']

        #ROW SELECTION WHERE WE WANT TO UPDATE THE DATA

        temp_dict={}
        temp_list=[]
        for i in rsp:
            Entry_ID=i['id']
            print(Entry_ID)

            if Entry_ID == d:
                break
            else:
                wks.insert_rows(row =1, number = 1)
    #         if not Entry_ID:
    #             print('entetred all values')
    #             break
    #         else:

                try:
                    Entry_Date=i['date_created']
                except:
                    Entry_Date=''
                try:
                    Form_ID=i['form_id']
                except:
                    Form_ID=''
                try:
                    First_Name=i['1.3']
                except:
                    First_Name=''
                try:
                    Last_Name=i['1.6']
                except:
                    Last_Name=''
                try:
                    Emails=i['2']
                except:
                    Emails=''
                try:
                    Mobile=i['4']
                except:
                    Mobile=''
                try:
                    DOB__Day =i['78']
                except:
                    DOB__Day =''
                try:
                    DOB__Month=i['79']
                except:
                    DOB__Month=''
                try:
                    DOB__Year=i['80']
                except:
                    DOB__Year=''
                try:
                    Country_1=i['61.6']
                except:
                    Country_1=''
                try:
                    Work_Address_Country=i['11.6']
                except:
                    Work_Address_Country=''
                try:
                    Gender=i['66']
                except:
                    Gender=''
                try:
                    Title=i['67']
                except:
                    Title=''
                try:
                    Years_with_bank=i['105']
                except:
                    Years_with_bank=''
                try:
                    Months_with_bank=i['106']
                except:
                    Months_with_bank=''
                try:
                    Referred=i['107']
                except:
                    Referred=''
                try:
                    IP_Address=i['ip']
                except:
                    IP_Address=''

                try:
                    Application_percent_Completed=i['required_fields_percent_complete']
                except:
                    Application_percent_Completed=''
                try:
                    Application_Status=i['workflow_step_status_8']
                except:
                    Application_Status=''

                try:
                    Work=i['77']
                except:
                    Work=''
            #     try:
            #         print(i['8'])
            #     except:
            #     try:
            #         print(i['16'])
            #     except:
                try:
                    Address_1=i['61.1']
                except:
                    Address_1=''
                try:
                    second_Address_Line_1=i['61.2']
                except:
                    second_Address_Line_1=''
                try:
                    City_1=i['61.3']
                except:
                    City_1=''
                try:
                    State_1=i['61.4']
                except:
                    State_1=''
                try:
                    ZIPpPost_Code=i['61.5']
                except:
                    ZIPpPost_Code=''
                try:
                    Living_Status=i['81']
                except:
                    Living_Status=''
                try:
                    Years_at_property_1=i['87']
                except:
                    Years_at_property_1=''
                try:
                    Months_at_property_1=i['88']
                except:
                    Months_at_property_1=''
                try:
                    Address_2=i['39.1']
                except:
                    Address_2=''
                try:
                    second_Address_Line_2=i['39.2']
                except:
                    second_Address_Line_2=''
                try:
                    City_2=i['39.3']
                except:
                    City_2=''
                try:
                    State_2=i['39.4']
                except:
                    State_2=''
                try:
                    ZIPpPost_Code_2=i['39.5']
                except:
                    ZIPpPost_Code_2=''
                try:
                    Country_2=i['39.6']
                except:
                    Country_2=''
                try:
                    Years_at_property_2=i['89']
                except:
                    Years_at_property_2=''
                try:
                    Months_at_property_2=i['90']
                except:
                    Months_at_property_2=''
                try:
                    Address_3=i['91.1']
                except:
                    Address_3=''
                try:
                    City_3=i['91.3']
                except:
                    City_3=''
                try:
                    State_3=i['91.4']
                except:
                    State_3=''
                try:
                    ZIPpPost_Code_3=i['91.5']
                except:
                    ZIPpPost_Code_3=''
                try:
                    Country_3=i['91.6']
                except:
                    Country_3=''
                try:
                    Referrer=i['60.3']
                except:
                    Referrer=''
                try:
                    Years_at_property_3=i['95']
                except:
                    Years_at_property_3=''
                try:
                    Months_at_property_3=i['96']
                except:
                    Months_at_property_3=''
                try:
                    Current_Employer=i['9']
                except:
                    Current_Employer=''
                try:
                    Job_Title=i['10']
                except:
                    Job_Title=''
                try:
                    Work_Address=i['11.1']
                except:
                    Work_Address=''
                try:
                    Work_Address_2nd_Line=i['11.2']
                except:
                    Work_Address_2nd_Line=''
                try:
                    Work_Address_City=i['11.3']
                except:
                    Work_Address_City=''
                try:
                    Work_Address_State=i['11.4']
                except:
                    Work_Address_State=''
                try:
                    Work_Address_ZIPpPost_Code=i['11.5']
                except:
                    Work_Address_ZIPpPost_Code=''
                try:
                    Years_with_current_employer=i['97']
                except:
                    Years_with_current_employer=''
                try:
                    Months_with_current_employer=i['98']
                except:
                    Months_with_current_employer=''
                try:
                    Previous_Work_Address=i['94.1']
                except:
                    Previous_Work_Address=''
                try:
                    Previous_Work_Address_2nd_Line=i['94.2']
                except:
                    Previous_Work_Address_2nd_Line=''
                try:
                    Previous_Work_Address_City=i['94.3']
                except:
                    Previous_Work_Address_City=''
                try:
                    Previous_Work_Address_State=i['94.4']
                except:
                    Previous_Work_Address_State=''
                try:
                    Previous_Work_Address_ZIPpPost_Code=i['94.5']
                except:
                    Previous_Work_Address_ZIPpPost_Code=''
                try:
                    Previous_Work_Address_Country=i['94.6']
                except:
                    Previous_Work_Address_Country=''
                try:
                    Years_with_previous_employer=i['103']
                except:
                    Years_with_previous_employer=''
                try:
                    Months_with_previous_employer=i['104']
                except:
                    Months_with_previous_employer=''
                try:
                    Annual_Salary=i['99']
                except:
                    Annual_Salary=''
                try:
                    Monthly_Wage=i['100']
                except:
                    Monthly_Wage=''
                try:
                    Bank_Name=i['102']
                except:
                    Bank_Name=''
                try:
                    Other_Bank=i['12']
                except:
                    Other_Bank=''
                try:
                    Account_Name=i['24']
                except:
                    Account_Name=''
                try:
                    Sort_Code=i['65']
                except:
                    Sort_Code=''
                try:
                    Account_Number=i['108']
                except:
                    Account_Number=''
                try:
                    Type_of_Vehicle=i['35']
                except:
                    Type_of_Vehicle=''
                try:
                    Fuel_Type=i['30']
                except:
                    Fuel_Type=''
                try:
                    Transmission_Type=i['33']
                except:
                    Transmission_Type=''
                try:
                    Age_of_required_vehicle=i['52']
                except:
                    Age_of_required_vehicle=''
                try:
                    Value_of_desired_car=i['101']
                except:
                    Value_of_desired_car=''
                try:
                    Deposit_willing_to_pay=i['48']
                except:
                    Deposit_willing_to_pay=''
                try:
                    Amount_over_1000=i['50']
                except:
                    Amount_over_1000=''
                try:
                    Vehicle_Use=i['34']
                except:
                    Vehicle_Use=''
                try:
                    Driving_Style=i['51']
                except:
                    Driving_Style=''
                try:
                    Expected_Mileage=i['53']
                except:
                    Expected_Mileage=''
                try:
                    Expected_Car_Ownership=i['54']
                except:
                    Expected_Car_Ownership=''
                try:
                    Purchase_at_End=i['55']
                except:
                    Purchase_at_End=''
                try:
                    Future_Payment_Issues=i['56']
                except:
                    Future_Payment_Issues=''
                try:
                    Employment_Issues=i['57']
                except:
                    Employment_Issues=''
                try:
                    Dream_Car_Link=i['58']
                except:
                    Dream_Car_Link=''
                try:
                    Resume_Application_URL=i['resume_url']
                except:
                    Resume_Application_URL=''
                try:
                    Referrer=i['60.3']
                except:
                    Referrer=''
                try:
                    Form_Source_URL=i['source_url']
                except:
                    Form_Source_URL=''

                print('\nnew id now..............................................')    


            #             temp_dict['registration']= registration
            temp_dict['cf_entry_id']= Entry_ID
            temp_dict['cf_entry_date']= Entry_Date
            temp_dict['cf_application_status']= Application_Status
            temp_dict['cf_application__complete']= Application_percent_Completed
            temp_dict['emails']= Emails
            temp_dict['cf_title']= Title
            temp_dict['first_name']= First_Name
            temp_dict['last_name']= Last_Name
            temp_dict['mobile_number']= Mobile
            temp_dict['work_number']= Work
            temp_dict['cf_gender']= Gender
            temp_dict['cf_dob__day']= DOB__Day
            temp_dict['cf_dob__month']= DOB__Month
            temp_dict['cf_dob__year']= DOB__Year
            temp_dict['address']= Address_1
            temp_dict['cf_address_2']= second_Address_Line_1
            temp_dict['city']= City_1
            temp_dict['state']= State_1
            temp_dict['zipcode']= ZIPpPost_Code
            temp_dict['country']= Country_1
            temp_dict['cf_living_status']= Living_Status
            temp_dict['cf_years_at_property_1']= Years_at_property_1
            temp_dict['cf_months_at_property']= Months_at_property_1
            temp_dict['cf_address2']= Address_2
            temp_dict['cf_2nd_address_line_2']= second_Address_Line_2
            temp_dict['cf_city_2']= City_2
            temp_dict['cf_state_2']= State_2
            temp_dict['cf_zippost_code_2']= ZIPpPost_Code_2
            temp_dict['cf_country_2']= Country_2
            temp_dict['cf_years_at_property_2']= Years_at_property_2
            temp_dict['cf_months_at_property_2']= Months_at_property_2
            temp_dict['cf_address_3']= Address_3
            temp_dict['cf_city_3']= City_3
            temp_dict['cf_state_3']= State_3
            temp_dict['cf_zippost_code_3']= ZIPpPost_Code_3
            temp_dict['cf_country_3']= Country_3
            temp_dict['cf_years_at_property_3']= Years_at_property_3
            temp_dict['cf_months_at_property_3']= Months_at_property_3
            temp_dict['cf_current_employer']= Current_Employer
            temp_dict['job_title']= Job_Title
            temp_dict['cf_work_address']= Work_Address
            temp_dict['cf_work_address_2nd_line']= Work_Address_2nd_Line
            temp_dict['cf_work_address_city']= Work_Address_City
            temp_dict['cf_work_address_state']= Work_Address_State
            temp_dict['cf_work_address_zippost_code']= Work_Address_ZIPpPost_Code
            temp_dict['cf_work_address_country']= Work_Address_Country
            temp_dict['cf_years_with_current_employer']= Years_with_current_employer
            temp_dict['cf_months_with_current_employer']= Months_with_current_employer
            temp_dict['cf_previous_work_address']= Previous_Work_Address
            temp_dict['cf_previous_work_address_2nd_line']= Previous_Work_Address_2nd_Line
            temp_dict['cf_previous_work_address_city']= Previous_Work_Address_City
            temp_dict['cf_previous_work_address_state']= Previous_Work_Address_State
            temp_dict['cf_previous_work_address_zippost_code']= Previous_Work_Address_ZIPpPost_Code
            temp_dict['cf_previous_work_address_country']= Previous_Work_Address_Country
            temp_dict['cf_years_with_previous_employer']= Years_with_previous_employer
            temp_dict['cf_months_with_previous_employer']= Months_with_previous_employer
            temp_dict['cf_annual_salary']= Annual_Salary
            temp_dict['cf_monthly_wage']= Monthly_Wage
            temp_dict['cf_bank_name']= Bank_Name
            temp_dict['cf_other_bank']= Other_Bank
            temp_dict['cf_account_name']= Account_Name
            temp_dict['cf_sort_code']= Sort_Code
            temp_dict['cf_account_number']= Account_Number
            temp_dict['cf_years_with_bank']= Years_with_bank
            temp_dict['cf_months_with_bank']= Months_with_bank
            temp_dict['cf_type_of_vehicle']= Type_of_Vehicle
            temp_dict['cf_fuel_type']= Fuel_Type
            temp_dict['cf_transmission_type']= Transmission_Type
            temp_dict['cf_age_of_required_vehicle']= Age_of_required_vehicle
            temp_dict['cf_value_of_desired_car']= Value_of_desired_car
            temp_dict['cf_deposit_willing_to_pay']= Deposit_willing_to_pay
            temp_dict['cf_amount_over_1000']= Amount_over_1000
            temp_dict['cf_vehicle_use']= Vehicle_Use
            temp_dict['cf_driving_style']= Driving_Style
            temp_dict['cf_expected_mileage']= Expected_Mileage
            temp_dict['cf_expected_car_ownership']= Expected_Car_Ownership
            temp_dict['cf_purchase_at_end']= Purchase_at_End
            temp_dict['cf_issue_with_future_payments']= Future_Payment_Issues
            temp_dict['cf_employment_issues']= Employment_Issues
            temp_dict['cf_dream_car_link']= Dream_Car_Link
            temp_dict['cf_referred']= Referred
            temp_dict['cf_referrer']= Referrer
            temp_dict['cf_ip_address']= IP_Address
            temp_dict['cf_resume_application_url']= Resume_Application_URL
            temp_dict['cf_form_source_url']= Form_Source_URL
            temp_dict['cf_form_id']= Form_ID
            temp_dict['status']= 0

            temp_list.append(temp_dict)
            temp_dict={}

        import pygsheets
        gc = pygsheets.authorize(service_file='main-project-366913.json')
        sh = gc.open('New Sheet')


        for t in temp_list:
                wks = sh[0] 

                cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
                last_row = len(cells)
                values = t.values()
                values_list = list(values)
                wks.update_row(update_row, values=[values_list], col_offset = 2)
                update_row = update_row +1







        sleep(2)    
        val=500
        pg =pg+500
        print(url)
        return Entry_ID
        
        
        
def complete_vals():
    import pygsheets
    import json
    import requests
    # url = 'https://halalcars.myfreshworks.com/crm/sales/api/contacts'
    count=1
    gc = pygsheets.authorize(service_file='main-project-366913.json')
    sh = gc.open('New Sheet')
    wks = sh[0] # select the first sheet
    read = wks.get_as_df()
    cars = wks.get_all_records()
    data = wks.get_all_records()
    
#     ID=int(EntryID)-1
    
    for car in range (0,len(cars)):
        count=count+1
        status=cars[car]['status']
        app_status=(cars[car]['cf_application_status'])
        ID=cars[car]['cf_entry_id']
        if status==1 :
            break
    #     else:
        elif app_status=='complete':

            cf_entry_id=cars[car]['cf_entry_id']
            # print(cf_entry_id)
            cf_entry_date=cars[car]['cf_entry_date']
            cf_application_status=cars[car]['cf_application_status']
            # print(cf_application_status)
            cf_application__complete=cars[car]['cf_application__complete']
            emails=cars[car]['emails']
            cf_title=cars[car]['cf_title']
            first_name=cars[car]['first_name']
            last_name=cars[car]['last_name']
            mobile_number=(cars[car]['mobile_number'])
            work_number=(cars[car]['work_number'])
            cf_gender=(cars[car]['cf_gender'])
            cf_dob__day=(cars[car]['cf_dob__day'])
            cf_dob__month=(cars[car]['cf_dob__month'])
            cf_dob__year=(cars[car]['cf_dob__year'])
            address=(cars[car]['address'])
            cf_address_2=(cars[car]['cf_address_2'])
            city=(cars[car]['city'])
            state=(cars[car]['state'])
            zipcode=(cars[car]['zipcode'])
            country=(cars[car]['country'])
            cf_living_status=(cars[car]['cf_living_status'])
            cf_years_at_property_1=(cars[car]['cf_years_at_property_1'])
            cf_months_at_property=(cars[car]['cf_months_at_property'])
            cf_address2=(cars[car]['cf_address2'])
            cf_2nd_address_line_2=(cars[car]['cf_2nd_address_line_2'])
            cf_city_2=(cars[car]['cf_city_2'])
            cf_state_2=(cars[car]['cf_state_2'])
            cf_zippost_code_2=(cars[car]['cf_zippost_code_2'])
            cf_country_2=(cars[car]['cf_country_2'])
            cf_years_at_property_2=(cars[car]['cf_years_at_property_2'])
            cf_months_at_property_2=(cars[car]['cf_months_at_property_2'])
            cf_address_3=(cars[car]['cf_address_3'])
            cf_city_3=(cars[car]['cf_city_3'])
            cf_state_3=(cars[car]['cf_state_3'])
            cf_zippost_code_3=(cars[car]['cf_zippost_code_3'])
            cf_country_3=(cars[car]['cf_country_3'])
            cf_years_at_property_3=(cars[car]['cf_years_at_property_3'])
            cf_months_at_property_3=(cars[car]['cf_months_at_property_3'])
            cf_current_employer=(cars[car]['cf_current_employer'])
            job_title=(cars[car]['job_title'])
            cf_work_address=(cars[car]['cf_work_address'])
            cf_work_address_2nd_line=(cars[car]['cf_work_address_2nd_line'])
            cf_work_address_city=(cars[car]['cf_work_address_city'])
            cf_work_address_state=(cars[car]['cf_work_address_state'])
            cf_work_address_zippost_code=(cars[car]['cf_work_address_zippost_code'])
            cf_work_address_country=(cars[car]['cf_work_address_country'])
            cf_years_with_current_employer=(cars[car]['cf_years_with_current_employer'])
            cf_months_with_current_employer=(cars[car]['cf_months_with_current_employer'])
            cf_previous_work_address=(cars[car]['cf_previous_work_address'])
            cf_previous_work_address_2nd_line=(cars[car]['cf_previous_work_address_2nd_line'])
            cf_previous_work_address_city=(cars[car]['cf_previous_work_address_city'])
            cf_previous_work_address_state=(cars[car]['cf_previous_work_address_state'])
            cf_previous_work_address_zippost_code=(cars[car]['cf_previous_work_address_zippost_code'])
            cf_previous_work_address_country=(cars[car]['cf_previous_work_address_country'])
            cf_years_with_previous_employer=(cars[car]['cf_years_with_previous_employer'])
            cf_months_with_previous_employer=(cars[car]['cf_months_with_previous_employer'])
            cf_annual_salary=(cars[car]['cf_annual_salary'])
            cf_monthly_wage=(cars[car]['cf_monthly_wage'])
            cf_bank_name=(cars[car]['cf_bank_name'])
            cf_other_bank=(cars[car]['cf_other_bank'])
            cf_account_name=(cars[car]['cf_account_name'])
            cf_sort_code=(cars[car]['cf_sort_code'])
            cf_account_number=(cars[car]['cf_account_number'])
            cf_years_with_bank=(cars[car]['cf_years_with_bank'])
            cf_months_with_bank=(cars[car]['cf_months_with_bank'])
            cf_type_of_vehicle=(cars[car]['cf_type_of_vehicle'])
            cf_fuel_type=(cars[car]['cf_fuel_type'])
            cf_transmission_type=(cars[car]['cf_transmission_type'])
            cf_age_of_required_vehicle=(cars[car]['cf_age_of_required_vehicle'])
            cf_value_of_desired_car=(cars[car]['cf_value_of_desired_car'])
            cf_deposit_willing_to_pay=(cars[car]['cf_deposit_willing_to_pay'])
            cf_amount_over_1000=(cars[car]['cf_amount_over_1000'])
            cf_vehicle_use=(cars[car]['cf_vehicle_use'])
            cf_driving_style=(cars[car]['cf_driving_style'])
            cf_expected_mileage=(cars[car]['cf_expected_mileage'])
            cf_expected_car_ownership=(cars[car]['cf_expected_car_ownership'])
            cf_purchase_at_end=(cars[car]['cf_purchase_at_end'])
            cf_issue_with_future_payments=(cars[car]['cf_issue_with_future_payments'])
            cf_employment_issues=(cars[car]['cf_employment_issues'])
            cf_dream_car_link=(cars[car]['cf_dream_car_link'])
            cf_referred=(cars[car]['cf_referred'])
            cf_referrer=(cars[car]['cf_referrer'])
            cf_ip_address=(cars[car]['cf_ip_address'])
            cf_resume_application_url=(cars[car]['cf_resume_application_url'])
            cf_form_source_url=(cars[car]['cf_form_source_url'])
            cf_form_id=(cars[car]['cf_form_id'])
            urll = 'https://halalcars.myfreshworks.com/crm/sales/api/contacts'
            data={
                "contact": {
                    "first_name": first_name,
                    "last_name": last_name,
                    "job_title": job_title,
                    "city": city,
                    "state": state,
                    "zipcode": zipcode,
                    "country": country,
                    "emails": emails,
                    "work_number": work_number,
                    "mobile_number":mobile_number,
                    "address": address,
                    "custom_field": {
                        "cf_title": cf_title,
                        "cf_gender": cf_gender,
                        "cf_dob__day": cf_dob__day,
                        "cf_dob__month": cf_dob__month,
                        "cf_dob__year": cf_dob__year,
                        "cf_address_2": cf_address_2,
                        "cf_living_status": cf_living_status,
                        "cf_years_at_property_1": cf_years_at_property_1,
                        "cf_months_at_property": cf_months_at_property,
                        "cf_entry_id": cf_entry_id,
                        "cf_entry_date": cf_entry_date,
                        "cf_application_status": cf_application_status,
                        "cf_application__complete": cf_application__complete,
                        "cf_resume_application_url": cf_resume_application_url,
                        "cf_form_source_url": cf_form_source_url,
                        "cf_form_id": cf_form_id,
            #             "cf_finance_form_status": cf_finance_form_status,
                        "cf_address2": cf_address2,
                        "cf_2nd_address_line_2": cf_2nd_address_line_2,
                        "cf_city_2": cf_city_2,
                        "cf_state_2": cf_state_2,
                        "cf_zippost_code_2": cf_zippost_code_2,
                        "cf_country_2": cf_country_2,
                        "cf_years_at_property_2": cf_years_at_property_2,
                        "cf_months_at_property_2": cf_months_at_property_2,
                        "cf_address_3": cf_address_3,
                        "cf_city_3": cf_city_3,
                        "cf_state_3": cf_state_3,
                        "cf_zippost_code_3": cf_zippost_code_3,
                        "cf_country_3": cf_country_3,
                        "cf_years_at_property_3": cf_years_at_property_3,
                        "cf_months_at_property_3": cf_months_at_property_3,
                        "cf_current_employer": cf_current_employer,
                        "cf_work_address": cf_work_address,
                        "cf_work_address_2nd_line": cf_work_address_2nd_line,
                        "cf_work_address_city": cf_work_address_city,
                        "cf_work_address_state": cf_work_address_state,
                        "cf_work_address_zippost_code": cf_work_address_zippost_code,
                        "cf_work_address_country": cf_work_address_country,
                        "cf_years_with_current_employer": cf_years_with_current_employer,
                        "cf_months_with_current_employer": cf_months_with_current_employer,
                        "cf_annual_salary": cf_annual_salary,
                        "cf_monthly_wage": cf_monthly_wage,
            #             "cf_previous_job_title": cf_previous_job_title,
                        "cf_previous_work_address": cf_previous_work_address,
                        "cf_previous_work_address_2nd_line": cf_previous_work_address_2nd_line,
                        "cf_previous_work_address_city": cf_previous_work_address_city,
                        "cf_previous_work_address_state": cf_previous_work_address_state,
                        "cf_previous_work_address_zippost_code": cf_previous_work_address_zippost_code,
                        "cf_previous_work_address_country": cf_previous_work_address_country,
                        "cf_years_with_previous_employer": cf_years_with_previous_employer,
                        "cf_months_with_previous_employer": cf_months_with_previous_employer,
                        "cf_bank_name": cf_bank_name,
                        "cf_account_name": cf_account_name,
                        "cf_sort_code": cf_sort_code,
                        "cf_account_number": cf_account_number,
                        "cf_years_with_bank": cf_years_with_bank,
                        "cf_months_with_bank": cf_months_with_bank,
                        "cf_other_bank": cf_other_bank,
                        "cf_fuel_type": cf_fuel_type,
                        "cf_type_of_vehicle": cf_type_of_vehicle,
                        "cf_value_of_desired_car": cf_value_of_desired_car,
                        "cf_vehicle_use": cf_vehicle_use,
                        "cf_transmission_type": cf_transmission_type,
                        "cf_deposit_willing_to_pay": cf_deposit_willing_to_pay,
                        "cf_amount_over_1000": cf_amount_over_1000,
                        "cf_driving_style": cf_driving_style,
                        "cf_age_of_required_vehicle": cf_age_of_required_vehicle,
                        "cf_expected_mileage": cf_expected_mileage,
                        "cf_expected_car_ownership": cf_expected_car_ownership,
                        "cf_purchase_at_end": cf_purchase_at_end,
                        "cf_issue_with_future_payments": cf_issue_with_future_payments,
                        "cf_employment_issues": cf_employment_issues,
                        "cf_dream_car_link": cf_dream_car_link,
                        "cf_referred": cf_referred,
                        "cf_referrer": cf_referrer,
                        "cf_ip_address": cf_ip_address,
                    } 
                }
            }
            headers = {'Authorization': 'Token token=zc49UdVMx8D9Y1m3gDkIAA','Content-Type': 'application/json'}
            r=requests.post(urll, data=json.dumps(data), headers=headers)
            # print(r.status_code)

def pending_greatest():
    ################### PENDING VALUES COMPARISON ####################################
    # Iterate over key/value pairs in dict and print them
    import pygsheets
    import requests
    import json
    gc = pygsheets.authorize(service_file='main-project-366913.json')
    sh = gc.open('New Sheet')
    wks = sh[0] # select the first sheet
    read = wks.get_as_df()
    cars = wks.get_all_records()
    data = wks.get_all_records()
    listt=[]
    Entry_ID=3239
    ID=Entry_ID-1
    for car in range (0,len(cars)):
        emails=cars[car]['emails']
        statuss=cars[car]['status']
        percent=cars[car]['cf_application__complete']
        stats=cars[car]['cf_application_status']


        for d in range(0,len(data)):
            emale= data[d]['emails']
            status=data[d]['status']
            prcnt=data[d]['cf_application__complete']
            stat=data[d]['cf_application_status']
            if emale==emails and status == 0 and percent!=prcnt and stats==stat :
                if emale=='':
                    ()
                else:
                    listt.append(data[d])
                break
        if statuss==1:
            break
    mail=''
    prcent=0
    lst=[]
    for value in listt:
        maile = value['emails']
        pcnt = value['cf_application__complete']

        pcnt1 = value['cf_application_status']
        if maile == mail:
            if pcnt > prcent and pcnt1=="pending" :
                cf_entry_id=value['cf_entry_id']
                # print(cf_entry_id)
                cf_entry_date=value['cf_entry_date']
                cf_application_status=value['cf_application_status']
                # print(cf_application_status)
                cf_application__complete=value['cf_application__complete']
                emails=value['emails']
                cf_title=value['cf_title']
                first_name=value['first_name']
                last_name=value['last_name']
                mobile_number=(value['mobile_number'])
                work_number=(value['work_number'])
                cf_gender=(value['cf_gender'])
                cf_dob__day=(value['cf_dob__day'])
                cf_dob__month=(value['cf_dob__month'])
                cf_dob__year=(value['cf_dob__year'])
                address=(value['address'])
                cf_address_2=(value['cf_address_2'])
                city=(value['city'])
                state=(value['state'])
                zipcode=(value['zipcode'])
                country=(value['country'])
                cf_living_status=(value['cf_living_status'])
                cf_years_at_property_1=(value['cf_years_at_property_1'])
                cf_months_at_property=(value['cf_months_at_property'])
                cf_address2=(value['cf_address2'])
                cf_2nd_address_line_2=(value['cf_2nd_address_line_2'])
                cf_city_2=(value['cf_city_2'])
                cf_state_2=(value['cf_state_2'])
                cf_zippost_code_2=(value['cf_zippost_code_2'])
                cf_country_2=(value['cf_country_2'])
                cf_years_at_property_2=(value['cf_years_at_property_2'])
                cf_months_at_property_2=(value['cf_months_at_property_2'])
                cf_address_3=(value['cf_address_3'])
                cf_city_3=(value['cf_city_3'])
                cf_state_3=(value['cf_state_3'])
                cf_zippost_code_3=(value['cf_zippost_code_3'])
                cf_country_3=(value['cf_country_3'])
                cf_years_at_property_3=(value['cf_years_at_property_3'])
                cf_months_at_property_3=(value['cf_months_at_property_3'])
                cf_current_employer=(value['cf_current_employer'])
                job_title=(value['job_title'])
                cf_work_address=(value['cf_work_address'])
                cf_work_address_2nd_line=(value['cf_work_address_2nd_line'])
                cf_work_address_city=(value['cf_work_address_city'])
                cf_work_address_state=(value['cf_work_address_state'])
                cf_work_address_zippost_code=(value['cf_work_address_zippost_code'])
                cf_work_address_country=(value['cf_work_address_country'])
                cf_years_with_current_employer=(value['cf_years_with_current_employer'])
                cf_months_with_current_employer=(value['cf_months_with_current_employer'])
                cf_previous_work_address=(value['cf_previous_work_address'])
                cf_previous_work_address_2nd_line=(value['cf_previous_work_address_2nd_line'])
                cf_previous_work_address_city=(value['cf_previous_work_address_city'])
                cf_previous_work_address_state=(value['cf_previous_work_address_state'])
                cf_previous_work_address_zippost_code=(value['cf_previous_work_address_zippost_code'])
                cf_previous_work_address_country=(value['cf_previous_work_address_country'])
                cf_years_with_previous_employer=(value['cf_years_with_previous_employer'])
                cf_months_with_previous_employer=(value['cf_months_with_previous_employer'])
                cf_annual_salary=(value['cf_annual_salary'])
                cf_monthly_wage=(value['cf_monthly_wage'])
                cf_bank_name=(value['cf_bank_name'])
                cf_other_bank=(value['cf_other_bank'])
                cf_account_name=(value['cf_account_name'])
                cf_sort_code=(value['cf_sort_code'])
                cf_account_number=(value['cf_account_number'])
                cf_years_with_bank=(value['cf_years_with_bank'])
                cf_months_with_bank=(value['cf_months_with_bank'])
                cf_type_of_vehicle=(value['cf_type_of_vehicle'])
                cf_fuel_type=(value['cf_fuel_type'])
                cf_transmission_type=(value['cf_transmission_type'])
                cf_age_of_required_vehicle=(value['cf_age_of_required_vehicle'])
                cf_value_of_desired_car=(value['cf_value_of_desired_car'])
                cf_deposit_willing_to_pay=(value['cf_deposit_willing_to_pay'])
                cf_amount_over_1000=(value['cf_amount_over_1000'])
                cf_vehicle_use=(value['cf_vehicle_use'])
                cf_driving_style=(value['cf_driving_style'])
                cf_expected_mileage=(value['cf_expected_mileage'])
                cf_expected_car_ownership=(value['cf_expected_car_ownership'])
                cf_purchase_at_end=(value['cf_purchase_at_end'])
                cf_issue_with_future_payments=(value['cf_issue_with_future_payments'])
                cf_employment_issues=(value['cf_employment_issues'])
                cf_dream_car_link=(value['cf_dream_car_link'])
                cf_referred=(value['cf_referred'])
                cf_referrer=(value['cf_referrer'])
                cf_ip_address=(value['cf_ip_address'])
                cf_resume_application_url=(value['cf_resume_application_url'])
                cf_form_source_url=(value['cf_form_source_url'])
                cf_form_id=(value['cf_form_id'])
                urll = 'https://halalcars.myfreshworks.com/crm/sales/api/contacts'
                data={
                    "contact": {
                        "first_name": first_name,
                        "last_name": last_name,
                        "job_title": job_title,
                        "city": city,
                        "state": state,
                        "zipcode": zipcode,
                        "country": country,
                        "emails": emails,
                        "work_number": work_number,
                        "mobile_number":mobile_number,
                        "address": address,
                        "custom_field": {
                            "cf_title": cf_title,
                            "cf_gender": cf_gender,
                            "cf_dob__day": cf_dob__day,
                            "cf_dob__month": cf_dob__month,
                            "cf_dob__year": cf_dob__year,
                            "cf_address_2": cf_address_2,
                            "cf_living_status": cf_living_status,
                            "cf_years_at_property_1": cf_years_at_property_1,
                            "cf_months_at_property": cf_months_at_property,
                            "cf_entry_id": cf_entry_id,
                            "cf_entry_date": cf_entry_date,
                            "cf_application_status": cf_application_status,
                            "cf_application__complete": cf_application__complete,
                            "cf_resume_application_url": cf_resume_application_url,
                            "cf_form_source_url": cf_form_source_url,
                            "cf_form_id": cf_form_id,
                #             "cf_finance_form_status": cf_finance_form_status,
                            "cf_address2": cf_address2,
                            "cf_2nd_address_line_2": cf_2nd_address_line_2,
                            "cf_city_2": cf_city_2,
                            "cf_state_2": cf_state_2,
                            "cf_zippost_code_2": cf_zippost_code_2,
                            "cf_country_2": cf_country_2,
                            "cf_years_at_property_2": cf_years_at_property_2,
                            "cf_months_at_property_2": cf_months_at_property_2,
                            "cf_address_3": cf_address_3,
                            "cf_city_3": cf_city_3,
                            "cf_state_3": cf_state_3,
                            "cf_zippost_code_3": cf_zippost_code_3,
                            "cf_country_3": cf_country_3,
                            "cf_years_at_property_3": cf_years_at_property_3,
                            "cf_months_at_property_3": cf_months_at_property_3,
                            "cf_current_employer": cf_current_employer,
                            "cf_work_address": cf_work_address,
                            "cf_work_address_2nd_line": cf_work_address_2nd_line,
                            "cf_work_address_city": cf_work_address_city,
                            "cf_work_address_state": cf_work_address_state,
                            "cf_work_address_zippost_code": cf_work_address_zippost_code,
                            "cf_work_address_country": cf_work_address_country,
                            "cf_years_with_current_employer": cf_years_with_current_employer,
                            "cf_months_with_current_employer": cf_months_with_current_employer,
                            "cf_annual_salary": cf_annual_salary,
                            "cf_monthly_wage": cf_monthly_wage,
                #             "cf_previous_job_title": cf_previous_job_title,
                            "cf_previous_work_address": cf_previous_work_address,
                            "cf_previous_work_address_2nd_line": cf_previous_work_address_2nd_line,
                            "cf_previous_work_address_city": cf_previous_work_address_city,
                            "cf_previous_work_address_state": cf_previous_work_address_state,
                            "cf_previous_work_address_zippost_code": cf_previous_work_address_zippost_code,
                            "cf_previous_work_address_country": cf_previous_work_address_country,
                            "cf_years_with_previous_employer": cf_years_with_previous_employer,
                            "cf_months_with_previous_employer": cf_months_with_previous_employer,
                            "cf_bank_name": cf_bank_name,
                            "cf_account_name": cf_account_name,
                            "cf_sort_code": cf_sort_code,
                            "cf_account_number": cf_account_number,
                            "cf_years_with_bank": cf_years_with_bank,
                            "cf_months_with_bank": cf_months_with_bank,
                            "cf_other_bank": cf_other_bank,
                            "cf_fuel_type": cf_fuel_type,
                            "cf_type_of_vehicle": cf_type_of_vehicle,
                            "cf_value_of_desired_car": cf_value_of_desired_car,
                            "cf_vehicle_use": cf_vehicle_use,
                            "cf_transmission_type": cf_transmission_type,
                            "cf_deposit_willing_to_pay": cf_deposit_willing_to_pay,
                            "cf_amount_over_1000": cf_amount_over_1000,
                            "cf_driving_style": cf_driving_style,
                            "cf_age_of_required_vehicle": cf_age_of_required_vehicle,
                            "cf_expected_mileage": cf_expected_mileage,
                            "cf_expected_car_ownership": cf_expected_car_ownership,
                            "cf_purchase_at_end": cf_purchase_at_end,
                            "cf_issue_with_future_payments": cf_issue_with_future_payments,
                            "cf_employment_issues": cf_employment_issues,
                            "cf_dream_car_link": cf_dream_car_link,
                            "cf_referred": cf_referred,
                            "cf_referrer": cf_referrer,
                            "cf_ip_address": cf_ip_address,
                        } 
                    }
                }
                headers = {'Authorization': 'Token token=zc49UdVMx8D9Y1m3gDkIAA','Content-Type': 'application/json'}
                r=requests.post(urll, data=json.dumps(data), headers=headers)
                # print(r.status_code)
                # print(data)

            else:
                prcent = pcnt
        else:
            mail= maile
            
from random import randint
from time import sleep        
def crm_API():
    idd=crm_Data()
    print(idd)
    print("complete_val is going to start in 1 minute")
    sleep(60)
    complete_vals()
    print("pending_greatest is going to start in 1 minute")
    sleep(60)
    pending_greatest()
    print("process is going to start in 10 to 15 minute")
    sleep(randint(600,900))
    crm_API()

crm_API()
# pending_greatest()