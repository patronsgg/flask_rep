from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ldjflkjdaf_lkjadlfkj_akldjflkjaflkjadljf'


class TestForm(FlaskForm):
    army_answer = RadioField(
        'Вы хотите служить?',
        choices=[('yes', 'КОНЕЧНО!'), ('no', 'Нет...')],
        validators=[DataRequired(message='НАДО ВЫБРАТЬ!')]
    )
    draw_answer = RadioField(
        'Красили ли вы газон у себя на участке?',
        choices=[('yes', 'Да, конечно.'), ('no', 'Нет, мне что нечем занятся')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    food_answer = RadioField(
        'Нравятся ли вам слипшиеся пельмени?',
        choices=[('yes', 'Да, мне такое нравится'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    bullying_answer = RadioField(
        'Готовы ли вы терпеть унижения от генералов?',
        choices=[('yes', 'ТАК ТОЧНО'), ('no', 'НИКАК НЕТ')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    submit = SubmitField('Узнать результат')


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if form.validate_on_submit():
        return render_template(
            'result.html',
            army=form.army_answer.data,
            draw=form.draw_answer.data,
            food=form.food_answer.data,
            bullying=form.bullying_answer.data
        )
    return render_template('test.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
