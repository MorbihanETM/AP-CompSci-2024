from flask import Flask
import random

app = Flask(__name__)

@app.route('/endpoint')
def roll_combat()-> str:
    x = random.randint(1, 20)
    if x == 1:
        return 'critical miss'
    if x == 20:
        return 'critical hit'
    else:
        final_damage = str(x)
        return 'you swing for ' + final_damage + ' damage'
    
@app.route('/advantage')
def roll_advantage()-> str:
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
        
@app.route('/disadvantage')
def roll_disadvantage()-> str:
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

def create_app():
    app = Flask(__name__)
    return app

if __name__ == '__main__':
    app.run(host = 'localhost', port = 8081)
    # app.run(debug=True)

