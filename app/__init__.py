import os
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import migrate
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config())

from app import routes
