from flask import Blueprint
from routes.api import get_company_investment_data_and_graph
import csv
import random

fyp_bp = Blueprint("fyp", __name__)
images = []
companies = []

@fyp_bp.route("/fyp", methods=["GET"])
def for_you():
    init_page()
    return "For You Page"

@fyp_bp.route("/fyp/refresh")
def refresh_Page():
    init_page()
    return

@fyp_bp.route("/fyp/investment")
def investment_popup():
    #click event
    
    return

def get_Top_Investments():  
    company_scores = []
    with open('backend/userDocs/stocks_data_with_scores.csv', mode = 'r') as file:
        csvFile = csv.reader(file)
        next(csvFile,None)

        for row in csvFile:
            company = row[0]
            stock_name = row[1]  
            score = row[6]  
            company_scores.append((company, stock_name, score))

    company_scores.sort(key=lambda x: x[1], reverse=True)   
    print(company_scores)
    return company_scores

def init_page():
    global companies 
    companies = get_Top_Investments()
    top_companies = [company for company, _ in companies[:4]]
    global images 
    images = get_company_investment_data_and_graph(top_companies[:4])
    return images
