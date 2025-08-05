from . import orders, order_details, recipes, sandwiches, resources

from ..dependencies.database import engine, Base


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)

def create_all_tables():
    Base.metadata.create_all(bind=engine)