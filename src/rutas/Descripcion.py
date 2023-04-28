from config.db import db, app, ma
from flask import Blueprint, Flask,  redirect, request, jsonify, json, session, render_template
routes_Descripcion = Blueprint("routes_Descripcion", __name__)


@routes_Descripcion.route('/indexDescripcion', methods=['GET'] )
def indexDescripcion():
    
    return render_template('/Main/Descripcion.html')