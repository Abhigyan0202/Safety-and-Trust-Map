from playwright.sync_api import sync_playwright
import time
from subs import get_substations
import pandas




def get_results(df,browser,substation,start_date,end_date):
    page = browser.new_page()
    try :
        page.goto("https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx")
        page.reload()
        time.sleep(4)
        page.locator("#ContentPlaceHolder1_ddlDistrict").select_option("BRIHAN MUMBAI CITY")
        page.locator("#ContentPlaceHolder1_ddlPoliceStation").select_option(substation)
        page.locator("#ContentPlaceHolder1_txtDateOfRegistrationFrom").press_sequentially(start_date)
        page.locator("#ContentPlaceHolder1_txtDateOfRegistrationTo").press_sequentially(end_date)
        page.click("#ContentPlaceHolder1_btnSearch")
        time.sleep(3)
        FIRs = page.locator("#ContentPlaceHolder1_lbltotalrecord").inner_text()
        print(f"{substation}, {start_date}, {end_date}, {FIRs} ")
        df.loc[len(df)] = [substation, start_date, end_date, FIRs]
        page.close()
    except :
        df.loc[len(df)] = [substation, start_date, end_date, -1] #-1 is to denote that data was not found for this entry for now
        print(f"{substation}, {start_date}, {end_date}, {-1} ")  #Due to website not loading 
            
def run(df,substations, start_date, end_date):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for s in substations:
            get_results(df,browser,s,start_date,end_date)
        browser.close()
        
       
        

if __name__ == "__main__":
    substations = get_substations()
    #supppose date is 01/08/2026, then we have to give it as input - 01082026
    months = [["01082026","31082026"],
              ["01072026","31072026"],
              ["01062026","30062026"],
              ["01052026","31052026"],
              ["01042026","30042026"],
              ["01032026","31032026"],
              ["01022026","28022026"],
              ["01012026","31012026"],
              ["01122025","31122025"],
              ["01112025","30112025"],
              ["01102025","31102025"],
              ["01092025","30092025"]]
    
    for i in range(12):
        df = pandas.DataFrame(columns=["Name", "StartDate","EndDate", "FIRs"])
        run(df, substations,months[i][0],months[i][1])
        df.to_csv(f"df_{months[i][0]}.csv")
