from party import create_app

if __name__ == '__main__':
    create_app().run(debug=True, host='localhost', port=5000)
