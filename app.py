from flask import Flask, request, render_template
from utils import gen_text

app = Flask(__name__, template_folder="template")


# @app.route('/')
@app.route('/textgen/', methods=['post', 'get'])
def login():
    message = ''
    if request.method == 'POST':
        prefix = request.form.get('prefix')
        temperature = request.form.get('temperature')
        min_length = request.form.get("min_length")
        max_length = request.form.get("max_length")

        generated_text = gen_text(min_length=min_length, max_length=max_length,
                                  temperature=temperature, sentence_prefix=prefix)

        if prefix == 'root':
            message = generated_text
        else:
            message = generated_text

    return render_template('index.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
