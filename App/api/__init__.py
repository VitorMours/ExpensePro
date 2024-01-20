from flask import Blueprint, jsonify


api_views = Blueprint('views', __name__)

@api_views.route('/', methods=["GET"])
def api_home():
    try:
        return jsonify({"Testando a api": True})
    except Exception:
        raise(Exception)
        