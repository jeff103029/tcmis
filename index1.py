from flask import Flask, render_template, request
from datetime import datetime
}
    "version": 2,
    "builds": [
        {
            "src": "./index.py",
            "use": "@vercel/python"
        }
    ],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "/"
        }
    ]
}

app = Flask(__name__)
…
#if __name__ == "__main__":
#    app.run()
