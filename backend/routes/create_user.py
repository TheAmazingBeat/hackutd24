from flask import Blueprint
import json
import os

create_user_bp = Blueprint("create_user", __name__)

curr_dir = os.getcwd()
fp = os.path.join(curr_dir, 'userDocs', 'userData.json')

@create_user_bp.route("/create_user")
def create_user():
    user = {
        "Name": "Leon Zhang",
        "Email": "leon.zh113@gmail.com",
        "Password": "test",
        "Account Balance": "$50,000",
        "Industry Preferences": ["Tech", "Finance", "Space"],
        "Investments": [("Apple", "AAPL", 5), ("X", "X", 10), ("Tesla", "TSLA", 2)],
        "Saved Investments": ["Meta", "Toyota"],
        "Term": "Short",
        "First Login": True
    }

    with open(fp, 'w') as f:
        json.dump(user, f)

    return ""

def load_json():
    with open(fp, "r") as f:
        data = json.load(f)
        return data
    

    
