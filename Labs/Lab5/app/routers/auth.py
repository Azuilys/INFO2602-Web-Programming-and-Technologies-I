from fastapi import APIRouter, HTTPException, Depends, Request, Response, Form
from sqlmodel import select
from app.database import SessionDep
from app.models import *
from app.utilities import flash
from app.auth import encrypt_password, verify_password, create_access_token, AuthDep
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from fastapi import status
from . import templates
from fastapi.responses import HTMLResponse, RedirectResponse

auth_router = APIRouter(tags=["Authentication"])

@auth_router.post("/login")
async def login_action(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: SessionDep,
    request: Request
) -> Response:
    # Implement task 3.3 here. Remove the line below that says "pass" once complete
    pass

@auth_router.post('/signup', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def signup_user(request:Request, db:SessionDep, username: Annotated[str, Form()], email: Annotated[str, Form()], password: Annotated[str, Form()],):
    # Implement task 3.4 here. Remove the line below that says "pass" once complete
    pass

@auth_router.get("/identify", response_model=UserResponse)
def get_user_by_id(db: SessionDep, user:AuthDep):
    return user


@auth_router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="login.html",
    )


@auth_router.get("/signup", response_class=HTMLResponse)
async def signup_page(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="signup.html",
    )