import os
from werkzeug.utils import secure_filename
from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app.main import main
from app.main.forms import NoteForm, TaskForm, ProfileForm
from app.models import db, Note, Task

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    note_form = NoteForm()
    task_form = TaskForm()
    
    # Notlar ve Görevler ileride şablonda (HTML) listelenecek
    # notes = current_user.notes
    # tasks = current_user.tasks
    
    # Henüz HTML kodlaması yapmadığımız için sadece ilgili değişkenleri render edeceğiz.
    return render_template('main/index.html', title='Panel', note_form=note_form, task_form=task_form)

@main.route('/note/add', methods=['POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(
            title=form.title.data,
            content=form.content.data,
            user_id=current_user.id
        )
        db.session.add(note)
        db.session.commit()
        flash('Not başarıyla eklendi.', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Not eklenirken hata: {error}', 'danger')
    return redirect(url_for('main.index'))

@main.route('/note/delete/<int:note_id>', methods=['POST'])
@login_required
def delete_note(note_id):
    # Güvenlik: Sadece current_user'a ait olan id'yi getir
    note = db.session.scalar(db.select(Note).where(Note.id == note_id, Note.user_id == current_user.id))
    if note:
        db.session.delete(note)
        db.session.commit()
        flash('Not silindi.', 'success')
    else:
        flash('Not bulunamadı veya silme yetkiniz yok.', 'danger')
    return redirect(url_for('main.index'))

@main.route('/task/add', methods=['POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Görev başarıyla eklendi.', 'success')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Görev eklenirken hata: {error}', 'danger')
    return redirect(url_for('main.index'))

@main.route('/task/delete/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    # Güvenlik: Sadece current_user'a ait olan id'yi getir
    task = db.session.scalar(db.select(Task).where(Task.id == task_id, Task.user_id == current_user.id))
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Görev silindi.', 'success')
    else:
        flash('Görev bulunamadı veya silme yetkiniz yok.', 'danger')
    return redirect(url_for('main.index'))

@main.route('/task/toggle/<int:task_id>', methods=['POST'])
@login_required
def toggle_task(task_id):
    # Güvenlik: Sadece current_user'a ait olan id'yi getir
    task = db.session.scalar(db.select(Task).where(Task.id == task_id, Task.user_id == current_user.id))
    if task:
        if task.status == 'Yapılacak':
            task.status = 'Bitti'
        else:
            task.status = 'Yapılacak'
        db.session.commit()
        flash('Görev durumu güncellendi.', 'success')
    else:
        flash('Görev bulunamadı veya güncelleme yetkiniz yok.', 'danger')
    return redirect(url_for('main.index'))

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        if form.picture.data:
            avatar_dir = os.path.join(current_app.root_path, 'static', 'avatars')
            os.makedirs(avatar_dir, exist_ok=True)
            
            original_filename = secure_filename(form.picture.data.filename)
            filename = f"user_{current_user.id}_{original_filename}"
            filepath = os.path.join(avatar_dir, filename)
            form.picture.data.save(filepath)
            
            current_user.avatar_img = filename

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Hesabınız başarıyla güncellendi.', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    avatar = current_user.avatar_img if current_user.avatar_img else 'default_avatar.png'
    avatar_file = url_for('static', filename='avatars/' + avatar)
    return render_template('main/profile.html', title='Profil', form=form, avatar_file=avatar_file)
