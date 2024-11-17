from flask import Blueprint
from routes.api import get_company_investment_data_and_graph
import json
import csv
import os
import random

fyp_bp = Blueprint("fyp", __name__)
curr_dir = os.getcwd()
stock_data_fp = os.path.join(curr_dir, 'userDocs', 'stocks_data_with_scores.csv')
user_data_fp = os.path.join(curr_dir, 'userDocs', 'stocks_data_with_scores.csv')
images = []
companies = []
currentComapnies = []


@fyp_bp.route("/fyp", methods=["GET"])
def for_you():
    init_page()
    return "For You Page"

# when user clicks refresh button
@fyp_bp.route("/fyp/refresh")
def refresh_Page():
    init_page()
    return

# When user clicks on a specific stock
@fyp_bp.route("/fyp/investment")
def investment_popup():
    return

# When user clicks yes to invest
@fyp_bp.route("/fyp/investment/yes")
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

# When user presses no on investment page
@fyp_bp.route("/fyp/investment/no")
def select_no(company):
    update_Current_Companies(company)
    return

def update_Current_Companies(company):
    global currentComapnies
    currentComapnies.remove(company)

def get_Top_Investments():  
    company_scores = []
    with open(stock_data_fp, mode = 'r') as file:
        csvFile = csv.reader(file)
        next(csvFile,None)

        for row in csvFile:
            company = row[0]
            stock_name = row[1]  
            score = row[6]  
            company_scores.append((company, stock_name, score))

    company_scores.sort(key=lambda x: x[2], reverse=True)   
    print(company_scores)
    return company_scores

def init_page():
    global companies 
    companies = get_Top_Investments()
    currentComapnies = [company[1] for company in companies[:4]]
    global images 
    images = get_company_investment_data_and_graph(currentComapnies[:4])

def load_json():
    with open(user_data_fp, "r") as f:
        data = json.load(f)
        return data
    
#helper methods to get list of images of the current dispalying companies
def get_images():
    return images

def get_current_companies():
    return currentComapnies
