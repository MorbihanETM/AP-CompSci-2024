import random
from flask import Blueprint

combat_bp = Blueprint('combat', __name__)

@combat_bp.route('/endpoint', methods=['GET'])
def roll_combat():
    x = random.randint(1, 20)
    if x == 1:
        return 'critical miss'
    if x == 20:
        return 'critical hit'
    else:
        final_damage = str(x)
        return 'you swing for ' + final_damage + ' damage'

@combat_bp.route('/advantage', methods=['GET'])
def roll_advantage(): 
    dice_1 = random.randint(1,20)
    dice_2 = random.randint(1,20)

    if dice_1 < dice_2:
        if dice_2 == 1:
            return 'critical miss'
        if dice_2 == 20:
            return 'critical hit'
        else:
            return 'you swing for ' + str(dice_2) + ' damage'
    if dice_2 < dice_1:
        if dice_1 == 1:
            return 'critical miss'
        if dice_1 == 20:
            return 'critical hit'
        else:
            return 'you swing for ' + str(dice_1) + ' damage'
    else:
        if dice_1 == 1:
            return 'critical miss'
        if dice_1 == 20:
            return 'critical hit'
        else:
            return 'you swing for ' + str(dice_1) + ' damage'

@combat_bp.route('/disadvantage', methods=['GET'])
def roll_disadvantage():
    dice_1 = random.randint(1,20)
    dice_2 = random.randint(1,20)

    if dice_1 > dice_2:
        if dice_2 == 1:
            return 'critical miss'
        if dice_2 == 20:
            return 'critical hit'
        else:
            return 'you swing for' + str(dice_2) + 'damage'
    if dice_2 > dice_1:
        if dice_1 == 1:
            return 'critical miss'
        if dice_1 == 20:
            return 'critical hit'
        else:
            return 'you swing for ' + str(dice_1) + ' damage'
    else:
        if dice_1 == 1:
            return 'critical miss'
        if dice_1 == 20:
            return 'critical hit'
        else:
            return 'you swing for ' + str(dice_1) + ' damage'
