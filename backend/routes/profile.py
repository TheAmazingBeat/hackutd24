from flask import Blueprint

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile", methods=["GET"])
def profile():
    return "Profile Page"

@profile_bp.route("/profile/edit", methods=["GET", "POST"])
def edit_profile():
    return "Edit Profile Page"
