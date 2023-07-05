import party.main as main

def create_app():
    return main.app

if __name__ == '__main__':
    create_app().run(debug=True, host='localhost', port=5000) #pragma: no cover
