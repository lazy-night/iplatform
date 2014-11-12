from web import app
from web.database import init_db

init_db()
app.run(host='0.0.0.0')
