from inspira import Inspira
from inspira.middlewares.sessions import SessionMiddleware

app = Inspira(secret_key="UXkuLh6o9VuNz5d7KSnxYW_y4zau2H3u0UEZMhWKsFsecoGhel")

session = SessionMiddleware()
app.add_middleware(session)
