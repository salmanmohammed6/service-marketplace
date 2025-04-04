from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

tasks = [
    {
        'title': 'Need plumbing repair',
        'location': 'Hyderabad',
        'payment': 2000,
        'deadline': '2024-02-10',
        'description': 'Leaking faucet needs repair',
        'category': 'Home Services'
    },
    {
        'title': 'Local guide needed for Charminar area',
        'location': 'Hyderabad',
        'payment': 1500,
        'deadline': '2024-02-09',
        'description': 'Need info on historical places and food spots',
        'category': 'Local Information'
    }
]

users = []

@main.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        flash('Login not implemented - this is a prototype.', 'info')
        return redirect(url_for('main.index'))
    return render_template('login.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        flash('Signup not implemented - this is a prototype.', 'info')
        return redirect(url_for('main.index'))
    return render_template('signup.html')

@main.route('/post', methods=['GET', 'POST'])
def post_service():
    if request.method == 'POST':
        task = {
            'title': request.form['title'],
            'location': request.form['location'],
            'payment': request.form['payment'],
            'deadline': request.form['deadline'],
            'description': request.form['description'],
            'category': request.form['category']
        }
        tasks.append(task)
        flash('Service posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('post_service.html')
