from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from flask_babel import Babel, _
from weasyprint import HTML
import io
from diagnostico import generar_diagnostico
from recomendaciones import generar_recomendaciones
from validacion import validar_datos

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Для flash-сообщений

# Настройки мультиязычности
app.config['BABEL_DEFAULT_LOCALE'] = 'ru'
app.config['BABEL_SUPPORTED_LOCALES'] = ['ru', 'es', 'en']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = './translations'

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.args.get('lang') or 'ru'

# Маршруты
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fisica', methods=['GET', 'POST'])
def fisica():
    if request.method == 'POST':
        datos_fisica = request.form.to_dict()
        errores = validar_datos(datos_fisica)
        if errores:
            for error in errores:
                flash(error)
            return render_template('form_fisica.html', datos=datos_fisica)
        return redirect(url_for('suavte', **datos_fisica))
    return render_template('form_fisica.html')

@app.route('/suavte', methods=['GET', 'POST'])
def suavte():
    if request.method == 'POST':
        datos_suavte = request.form.to_dict()
        errores = validar_datos(datos_suavte)
        if errores:
            for error in errores:
                flash(error)
            return render_template('form_suavte.html', datos=datos_suavte)
        return redirect(url_for('columna', **datos_suavte))
    return render_template('form_suavte.html')

@app.route('/columna', methods=['GET', 'POST'])
def columna():
    if request.method == 'POST':
        datos_columna = request.form.to_dict()
        errores = validar_datos(datos_columna)
        if errores:
            for error in errores:
                flash(error)
            return render_template('form_columna.html', datos=datos_columna)
        return redirect(url_for('dinamica', **datos_columna))
    return render_template('form_columna.html')

@app.route('/dinamica', methods=['GET', 'POST'])
def dinamica():
    if request.method == 'POST':
        datos_dinamica = request.form.to_dict()
        errores = validar_datos(datos_dinamica)
        if errores:
            for error in errores:
                flash(error)
            return render_template('form_dinamica.html', datos=datos_dinamica)
        return redirect(url_for('resultados', **datos_dinamica))
    return render_template('form_dinamica.html')

@app.route('/resultados', methods=['GET', 'POST'])
def resultados():
    datos = request.args.to_dict()
    hipotesis = generar_diagnostico(datos)
    recomendaciones = generar_recomendaciones(datos)
    if request.method == 'POST':
        # Генерация PDF
        rendered = render_template('pdf_template.html', resultados=datos, hipotesis=hipotesis, recomendaciones=recomendaciones)
        pdf = HTML(string=rendered).write_pdf()
        buffer = io.BytesIO(pdf)
        buffer.seek(0)
        return send_file(buffer, as_attachment=True, download_name="resultados.pdf", mimetype="application/pdf")
    return render_template('resultados.html', resultados=datos, hipotesis=hipotesis, рекомендации=recomendaciones)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
