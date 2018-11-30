from flask import Flask
from api.views import ireporterViews


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(ireporterViews.bp)