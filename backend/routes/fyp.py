from flask import Blueprint
from routes.api import get_company_investment_data_and_graph, get_company_summary, get_current_stock_price
import pandas as pd
import json
import csv
import os
import random

fyp_bp = Blueprint("fyp", __name__)
curr_dir = os.getcwd()
print(curr_dir)
result_fp = os.path.join(curr_dir, 'model', 'result.csv')
user_data_fp = os.path.join(curr_dir, 'userDocs', 'userData.json')
stock_data_fp = os.path.join(curr_dir, 'model', 'stocks_data.csv')
images = []
companies = []
currentComapnies = []


@fyp_bp.route("/fyp", methods=["GET"])
def for_you():
    return init_page()

# when user clicks refresh button
@fyp_bp.route("/fyp/refresh")
def refresh_Page():
    df = pd.read_csv(stock_data_fp)
    for company in currentComapnies:
        df.loc[df['Company Name'] == company, 'User Decision'] == "No"
    df.to_csv(stock_data_fp, index = False)

    init_page()
    return

# When user clicks on a specific stock
@fyp_bp.route("/fyp/investment")
def investment_popup(company):
    return get_company_summary(company)

@fyp_bp.route("/fyp/investment/yes")
def user_click_yes(company):
    df = pd.read_csv(stock_data_fp)
    df.loc[df['Company Name'] == company, 'User Decision'] == "Yes"
    df.to_csv(stock_data_fp, index = False)

# When user clicks confirm investment amount
@fyp_bp.route("/fyp/investment/yes/confirm")
def enter_investment_amount(company, stock_name, investment_amount, num_of_stocks):
    user_data = load_json()
    user_data["Account Balance"] = user_data["Account Balance"] - investment_amount
    user_data["Investments"].append((company, stock_name, num_of_stocks))
    json.dump(user_data, user_data_fp)


# When user presses save button
@fyp_bp.route("/fyp/investments/save")
def save_investment(company):
    user_data = load_json()
    user_data["Saved Investments"].append(company)
    json.dump(user_data, user_data_fp)
    df = pd.read_csv(stock_data_fp)
    df.loc[df['Company Name'] == company, 'User Decision'] == "Maybe"
    df.to_csv(stock_data_fp, index = False)


# When user presses no on investment page
@fyp_bp.route("/fyp/investment/no")
def select_no(company):
    update_Current_Companies(company)
    df = pd.read_csv(stock_data_fp)
    df.loc[df['Company Name'] == company, 'User Decision'] == "No"
    df.to_csv(stock_data_fp, index = False)

def update_Current_Companies(company):
    global currentComapnies
    currentComapnies.remove(company)

def get_Top_Investments():  
    excluded_companies = set()
    with open(stock_data_fp, mode='r') as stock_file:
        stock_reader = csv.DictReader(stock_file)
        for row in stock_reader:
            if row["User Decision"] == "No":
                excluded_companies.add(row["Company Name"])

    company_info = []
    with open(stock_data_fp, mode = 'r') as file:
        csvFile = csv.reader(file)
        next(csvFile,None)

        for row in csvFile:
            company = row[1]
            stock_name = row[2]  
            industry = row[3]
            price_change = row[5]
            score = row[7]
            image = ""  
            
            if company not in excluded_companies: 
                company_info.append({
                    "company": company,
                    "stock_name": stock_name,
                    "industry": industry,
                    "current_price": 0,
                    "price_change": price_change,
                    "score": score,
                    "image": ""  # Placeholder for the image
                })
    company_info.sort(key=lambda x: x["score"], reverse=True)
    return company_info

def init_page():
    global companies
    companies = get_Top_Investments()
    top_companies = [company["stock_name"] for company in companies[:4]]
    images = get_company_investment_data_and_graph(top_companies[:4])
    prices = get_current_stock_price(top_companies[:4])

    for i, image in enumerate(images):
        companies[i]["image"] = image  
        companies[i]["current_price"] = prices

    return json.dumps(companies[:4])  

def load_json():
    with open(user_data_fp, "r") as f:
        data = json.load(f)
        return data
    
#helper methods to get list of images of the current dispalying companies
def get_images():
    return images

def get_current_companies():
    return currentComapnies
