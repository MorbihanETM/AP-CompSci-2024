from flask import Blueprint

combat_bp = Blueprint('combat', __name__)

@combat_bp.route('/endpoint', methods=['GET'])
def roll_combat():
    return 'Combat roll endpoint'

@combat_bp.route('/advantage', methods=['GET'])
def roll_advantage(): 
    return 'Advantage roll endpoint'

@combat_bp.route('/disadvantage', methods=['GET'])
def roll_disadvantage():
    return 'Disadvantage roll endpoint'
