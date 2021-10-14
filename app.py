
from flask import Flask, request, render_template
from leagueinputs import InputForm
from analyzer import analyzer

app = Flask(__name__)

@app.route('/league_details', methods=['GET','POST'])
def index():
    template = 'input.html'
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = analyzer(form.league_id.data, form.year.data,
                        form.espn_s2.data, form.swid.data)
    else:
        result = None

    return render_template(template,form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
