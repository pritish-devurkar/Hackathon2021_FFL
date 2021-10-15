
from flask import Flask, request, render_template, redirect, url_for
from leagueinputs import InputForm, SelectFormList
from analyzer import player_lists

app = Flask(__name__)

@app.route('/league_details', methods=['GET','POST'])
def index():
    template = 'input.html'
    
    form = InputForm(request.form)
    
    if request.method == 'POST' and form.validate():
        result = player_lists(form.league_id.data, form.year.data,
                        form.espn_s2.data, form.swid.data)
        print(result)
        # return redirect(url_for('trade_analyzer'))
    else:
        result = None

    return render_template(template,form=form, result=result)

@app.route('/trade_analyzer', methods=['POST'])
def trade_analyzer():
    template1 = 'trades.html'
    result2 = request.form('result')
    player_fields = [
        {"name": "Player Name1"},
        {"name": "Player Name2"}
    ]
    form2 = SelectFormList(players=player_fields)
    return render_template(template1, result2=result2)


if __name__ == '__main__':
    app.run(debug=True)
