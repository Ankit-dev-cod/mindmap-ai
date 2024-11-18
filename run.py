from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default a 5000 se la variabile PORT non è definita
    app.run(host='0.0.0.0', port=port)
