# A very simple web app to complete a GPT3 prompt

from flask import Flask, request
from runGPT import run_GPT


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        prompt = None
        if prompt is not None:
            result = run_GPT(prompt)
            return '''
                <html>
                    <body>
                        <p>The machine says {result}</p>
                        <p><a href="/">Click here to run it back</a>
                    </body>
                </html>
            '''.format(result=result)
    return '''
        <html>
            <body>
                {errors}
                <p>Enter your prompt:</p>
                <form method="post" action=".">
                    <p><input name="prompt" /></p>
                    <p><input type="submit" value="Make GPT Request" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)
