from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_descripcion = Blueprint("routes_descripcion", __name__)


@routes_descripcion.route('/descripcion', methods=['GET'] )
def descripcion():
    
    return render_template('/Main/descrip.html')