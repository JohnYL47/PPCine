from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_mainlogin = Blueprint("routes_mainlogin", __name__)


@routes_mainlogin.route('/indexmainlogin', methods=['GET'] )
def indexmainlogin():
    
    return render_template('/Main/MainLogin.html')