# Flask — Quick Cheatsheet

## Minimal app (factory pattern)
```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    app.config['JSON_SORT_KEYS'] = False
    db.init_app(app)

    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({'status': 'ok'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```