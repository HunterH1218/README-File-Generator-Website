import system
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        response = system.generate_readme(prompt)
        return render_template('index.html', prompt=prompt, response=response)
    return render_template('index.html', prompt='', response='')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)