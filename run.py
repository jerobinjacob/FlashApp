from webapp import sep_app
app = sep_app()
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5050, debug = True)