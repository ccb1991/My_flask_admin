"""
Created by 陈辰柄 
datetime:2019/9/25 22:13
Describe:
"""
import os

from app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")

if __name__ == '__main__':
    app.run(debug=True)
