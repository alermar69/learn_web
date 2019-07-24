from flask import Flask
from weather import weather_by_sity

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_sity('Moscow,Russia')
    if weather:
        return f'Погода: {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}'
    else:
        return 'Сервис погоды временно не доступен'

if __name__ == '__main__':
    app.run(debug=True)