from route import combat_bp
from flask import Flask, render_template
    
# Create a function defining the app in flask
def create_app():
    app = Flask(__name__)

# Register the Blueprint to the app
    app.register_blueprint(combat_bp)
    return app

app = Flask(__name__)

IMG_DIR = './static'

@app.route('/image')
def serve_image():
    "a simple HTTP image"
    return render_template('image.html')

if __name__ == '__main__':
    app = create_app()
    app.run(host = 'localhost', port = 8081)

