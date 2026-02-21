from typing import Annotated
import typer
from app.database import create_db_and_tables, get_session, drop_all
from app.models import User
from fastapi import Depends
from sqlmodel import select
from sqlalchemy.exc import IntegrityError

cli = typer.Typer()

@cli.command()
def initialize():
    """
    Recreates the database from scratch and adds a default user 'bob'.
    """
    with get_session() as db:
        drop_all()  # Delete all tables
        create_db_and_tables()  # Recreate all tables
        bob = User('bob', 'bob@mail.com', 'bobpass')
        db.add(bob)
        db.commit()
        db.refresh(bob)
        print("Database Initialized")


@cli.command()
def get_user(
    username: Annotated[str, typer.Argument(help="The username of the user to retrieve")]
):
    """
    Retrieve a single user from the database by username.
    Prints the user details or a friendly message if not found.
    """
    with get_session() as db:
        user = db.exec(select(User).where(User.username == username)).first()
        if not user:
            print(f"{username} not found!")
            return
        print(user)


@cli.command()
def get_all_users():
    """
    Retrieve all users in the database.
    Prints a list of all users or a message if no users exist.
    """
    with get_session() as db:
        all_users = db.exec(select(User)).all()
        if not all_users:
            print("No users found")
            return
        for user in all_users:
            print(user)


@cli.command()
def change_email(
    username: Annotated[str, typer.Argument(help="The username of the user to update")],
    new_email: Annotated[str, typer.Argument(help="The new email to assign to the user")]
):
    """
    Change the email of an existing user identified by username.
    """
    with get_session() as db:
        user = db.exec(select(User).where(User.username == username)).first()
        if not user:
            print(f'{username} not found! Unable to update email.')
            return
        user.email = new_email
        db.add(user)
        db.commit()
        print(f"Updated {user.username}'s email to {user.email}")


@cli.command()
def create_user(
    username: Annotated[str, typer.Argument(help="The username of the new user")],
    email: Annotated[str, typer.Argument(help="The email of the new user")],
    password: Annotated[str, typer.Argument(help="The password of the new user")]
):
    """
    Creates a new user in the database.
    Handles duplicate usernames or emails gracefully.
    """
    with get_session() as db:
        newuser = User(username, email, password)
        try:
            db.add(newuser)
            db.commit()
        except IntegrityError:
            db.rollback()
            print("Username or email already taken!")
        else:
            print(newuser)


@cli.command()
def delete_user(
    username: Annotated[str, typer.Argument(help="The username of the user to delete")]
):
    """
    Deletes a user from the database by username.
    """
    with get_session() as db:
        user = db.exec(select(User).where(User.username == username)).first()
        if not user:
            print(f'{username} not found! Unable to delete user.')
            return
        db.delete(user)
        db.commit()
        print(f'{username} deleted')


@cli.command()
def get_user_email_username(
    email: Annotated[str, typer.Argument(help="The email to search for")],
    username: Annotated[str, typer.Argument(help="The username to search for")]
):
    """
    Retrieve a user by email OR username.
    Prints the user details or message if not found.
    """
    with get_session() as db:
        user = db.exec(
            select(User).where((User.email == email) | (User.username == username))).first()
        if not user:
            print('No user found with that email or username!')
            return
        print(user)


@cli.command()
def list_users(
    limit: Annotated[int, typer.Argument(help="Number of users to retrieve [default: 10]")] = 10,
    offset: Annotated[int, typer.Argument(help="Start retrieving users from this index [default: 0]")] = 0
):
    """
    List a subset of users for pagination.
    """
    with get_session() as db:
        users = db.exec(select(User).offset(offset).limit(limit)).all()
        if not users:
            print("No users found in this range!")
            return
        for user in users:
            print(user)


if __name__ == "__main__":
    cli()