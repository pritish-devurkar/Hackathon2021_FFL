from wtforms import Form, IntegerField, StringField, validators, SelectField, FieldList, FormField


class InputForm(Form):
    league_id = IntegerField(
        label='League ID',
        validators=[validators.InputRequired()]
    )
    year = IntegerField(
        label='Year', default=2021,
        validators=[validators.InputRequired()]
    )
    espn_s2 = StringField(
        label='ESPN_S2',
        validators=[validators.InputRequired()]
    )
    swid = StringField(
        label='swid',
        validators=[validators.InputRequired()]
    )
class TradeForms(Form):
    name = SelectField("Placeholder", choices=[])

class SelectFormList(Form):
    name_entries = FieldList(FormField(TradeForms))