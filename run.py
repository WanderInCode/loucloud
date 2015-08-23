# from loucloud import create_app, db, DEFAULT_BLUEPRINTS
from loucloud import app

# app = create_app(blueprints=DEFAULT_BLUEPRINTS)

app.run(debug=True, port=5000)
