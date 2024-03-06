from flask import Flask

from main.main.main_endpoint import main_blueprint
from main.shipping_code.tracking_number_endpoint import tracking_number_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(tracking_number_blueprint)

if __name__ == "__main__":
    app.run()
