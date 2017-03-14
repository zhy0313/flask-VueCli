from social import app, database

if __name__ == '__main__':
    database.create_all()
    app.run(debug=True)
