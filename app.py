from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_unoque_secret_key'


@app.route('/', methods=["GET","POST"]) #here mai GET  Request add kiya apne se 
def index():
    if request.method == 'POST':
        if request.form['submit_note'] == 'add':
            current_notes = session['notes']
            note = request.form['note']
            if bool(note) & (note not in current_notes):
                current_notes.append(note)
        else:
            del_notes = request.form.getlist('del_notes')
            current_notes = session['notes']
            for note in del_notes:
                if note in current_notes:
                    current_notes.remove(note)
        session['notes'] = current_notes
    else:
        if 'notes' not in session:
            session['notes'] = []
    return render_template('index.html', notes=session['notes'])

if __name__ == '__main__':
    app.run(debug=True)