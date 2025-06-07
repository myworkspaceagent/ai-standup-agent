
from fastapi import FastAPI
from api import summary
from api import auth
from api import user
app = FastAPI()

app.include_router(summary.router)
# Check this prefix
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")
app.include_router(summary.router, prefix="/generate")