from flask import Flask, request, render_template
from utils import gen_text

app = Flask(__name__, template_folder="template")


@app.route('/', methods=['post', 'get'])
@app.route('/index', methods=['post', 'get'])
def textgen():
    if request.method == 'POST':
        prefix = request.form.get('prefix')
        temperature = request.form.get('temperature')
        min_length = request.form.get("min_length")
        max_length = request.form.get("max_length")

        generated_text = gen_text(min_length=min_length, max_length=max_length,
                                  temperature=temperature, sentence_prefix=prefix)

        return render_template('index.html', message=generated_text)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=500, use_reloader=True)
