from main import create_app
from backend.database.config import DevConfig, ProdConfig

app = create_app(ProdConfig)

if __name__ == "__main__":
    app.run()