from app import app
from creata_table import create_tables

db._init_app(app)


@app.before_first_request
def create_tables():
    create_tables.tables_creation()
