from flask import Blueprint
import json

create_user_bp = Blueprint("create_user", __name__)
    

@create_user_bp.route("/create_user")
def create_user():
    user = {
        "Name": "Leon Zhang",
        "Email": "leon.zh113@gmail.com",
        "Password": "test",
        "Account Balance": "$50,000",
        "Industry Preferences": ["Tech", "Finance", "Space"],
        "Term": "Short",
        "First Login": True
    }

    with open('backend/userDocs/userData.json', 'w') as f:
        json.dump(user, f)

    return ""

def load_json():
    with open('backend/userDocs/userData.json', "r") as f:
        data = json.load(f)
        return data["First Login"]
    

    
