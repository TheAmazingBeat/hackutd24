from flask import Blueprint
import json
from routes.api import get_company_investment_data_and_graph
import os

curr_dir = os.getcwd()
fp = os.path.join(curr_dir, 'userDocs', 'userData.json')
images = []
investments = []

investments_bp = Blueprint("investments", __name__)

#gets the list of all the user's investments
@investments_bp.route("/investments", methods=["GET"])
def get_investments():
    user_data = load_json()
    global investments, images
    investments = user_data["Investments"]
    investments = [company[1] for company in investments]
    print(investments)
    images = get_company_investment_data_and_graph(investments)
    return "hello"


def load_json():
    with open(fp, "r") as f:
        data = json.load(f)
        return data
    
#helper methods to get list of images of the current dispalying companies
def get_images():
    return images

def get_current_companies():
    return investments