from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_recruto():
    # Получаем параметры из запроса
    name = request.args.get('name', 'Recruto')  # Если параметр не указан, используем 'Recruto' по умолчанию
    message = request.args.get('message', 'Давай дружить!')  # Если параметр не указан, используем 'Давай дружить' по умолчанию
    
    # Формируем ответ
    return f"Hello {name}! {message}"

if __name__ == '__main__':
    print('\nCopy link to visit WebSite: http://127.0.0.1:5000/?name=Recruto&message=Давай%20дружить\n')
    app.run(debug=True)

    
