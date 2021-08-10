from flask import render_template, request, redirect, session
from flask_app import app
from flask_bcrypt import Bcrypt
from ..models.user import User