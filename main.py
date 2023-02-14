from flask import Flask
from flask import url_for
from flask import request
from random import choice

app = Flask(__name__)


@app.route("/")
def start():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def return_sample_page():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Colonization</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                  </body>
     
                </html>"""


@app.route("/image_mars")
def mars_im():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    
                  </body>"""


@app.route("/promotion_image")
def prom_im():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style.css")}" />
                     <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="/static/img/mars.png" alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-dark" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                    
                  </body>"""


@app.route("/astronaut_selection", methods=["POST", "GET"])
def form_sample():
    if request.method == "GET":
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for("static", filename="css/style1.css")}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2>Анкета претендента</h2>
                            <h4>на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="fam" class="form-control" id="fam" aria-describedby="emailHelp" placeholder="Введите фамилию" name="fam">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <label for="classSelect"></label>
                                    <input type="email" class="form-control" id="email" placeholder="Введите email" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="class" name="class">
                                          <option>Начальное</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                          <option>Отсутствует</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="form-check">Какие у вас есть профессии?</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="research-engineer" value="research-engineer">
                                          <label class="form-check-label" for="male">
                                            Инженер-исследователь
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="building engineer" value="building engineer">
                                          <label class="form-check-label" for="male">
                                            Инженер строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="pilot">
                                          <label class="form-check-label" for="male">
                                            Пилот
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="builder" value="builder">
                                          <label class="form-check-label" for="male">
                                            Строитель
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="exobiologist" value="exobiologist">
                                          <label class="form-check-label" for="male">
                                            Экзобиолог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="meteorologist" value="meteorologist">
                                          <label class="form-check-label" for="male">
                                            Метеоролог
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="doctor" value="doctor">
                                          <label class="form-check-label" for="male">
                                            Врач
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="checkbox" name="profession" id="pilot" value="Climatolog"
                                          <label class="form-check-label" for="male">
                                            Климатолог
                                          </label>
                                        </div>
                                        
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == "POST":
        print(request.form["email"])
        print(request.form["name"])
        print(request.form["fam"])
        print(request.form["class"])
        print(request.form["file"])
        print(request.form.get("accept"))
        print(request.form["sex"])
        print(request.form["about"])
        print(request.form)
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def planet_info(planet_name):
    text = {"Меркурий": ["Ближайшая к Солнцу планета", "Наименьшая планета системы", "Назван в честь бога торговли",
                         "Нет атмосферы"],
            "Венера": ["Вторая планета Солнечной системы", "Планета земной группы", "Названа в честь богини любви",
                       "Есть атмосфера"],
            "Земля": ["Третья планета Солнечной системы", "Планета земной группы", "Планета, где есть жизнь",
                      "Есть атмосфера"],
            "Марс": ["Четвертая планета Солнечной системы", "Планета земной группы", "Назван в честь бога войны",
                     "Нет атмосферы"],
            "Юпитер": ["Пятая планета Солнечной системы", "Газообразная планета", "Назван в честь бога громовержца",
                       "Самая большая планета Солнечной системы"],
            "Сатурн": ["Шестая планета Солнечной системы", "Газообразная планета", "Назван в честь бога земледелия",
                       "Вторая по размеру планета Солнечной системы"],
            "Уран": ["Седьмая планета Солнечной системы", "Газообразная планета", "Назван в честь бога неба",
                     "Относится к холодным газовым гигантам"],
            "Нептун": ["Восьмая планета Солнечной системы", "Газообразная планета", "Назван в честь бога моря",
                       "Относится к холодным газовым гигантам"],
            "А такой нет": ["Вы что-то напутали", "Такой планеты в нашей системе нет"],
            "Плутон": ["С 2008 года он больше не планета", "он относится к Карликовым планетам"]}
    if planet_name not in text:
        planet_name = "А такой нет"
    colors = ["dark", "success", "secondary", "warning", "danger", "primary", "info", "light"]
    html_text = "".join([f"""<div class="alert alert-{choice(colors)}" role="alert">
  {i}
</div>""" for i in text[planet_name]])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Варианты выбора</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                  </body>
                  {html_text}
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def test(nickname, level, rating):
    colors = ["success", "warning", "danger"]
    if rating <= 50:
        clr = colors[2]
    elif rating <= 75:
        clr = colors[1]
    else:
        clr = colors[0]
    html_text = f"""<div class="alert alert-{clr}" role="alert">Поздравляем! Ваш рейтинг после {level} этапа 
    отбора:</div> """
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Результаты</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <h4>{html_text}
                    составляет {rating}!
                    <div class="alert alert-info" role="alert">Желаем удачи!</div></h4>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")
