#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

page = Blueprint('home_page', __name__, template_folder='templates/home')

@page.route("/")
def index():
    return render_template("home/index.html")
