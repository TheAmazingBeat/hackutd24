from flask import Blueprint
from routes.api import get_company_investment_data_and_graph

investments_bp = Blueprint("investments", __name__)

@investments_bp.route("/investments", methods=["GET"])
def investments():
    return "Investments Overview"

@investments_bp.route("/investments/<int:investment_id>", methods=["GET"])
def investment_details(investment_id):
    return f"Details of Investment {investment_id}"
