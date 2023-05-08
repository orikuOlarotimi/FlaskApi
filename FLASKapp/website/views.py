from flask import Blueprint, render_template, request,flash
from flask_login import login_required, current_user
from .models import Note
from . import db
views = Blueprint('views', __name__)


@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('note is too short',category='error')
        else:
            new_note = Note(data=note)
            new_note.save()
            flash('Note has been added',category='sucess')
    return render_template("home.html", user=current_user)
