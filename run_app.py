from app import factory

if __name__ == "__main__":
    app = factory.create_app()
    app.run("0.0.0.0", port=5000, threaded=4)
