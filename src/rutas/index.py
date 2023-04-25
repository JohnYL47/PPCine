from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_index = Blueprint("routes_index", __name__)


@routes_index.route('/indexMain', methods=['GET'] )
def indexMain():
    
    return render_template('/Main/Main.html')