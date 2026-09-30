import os
from flask import Flask, render_template, send_from_directory

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin.html")
@app.route("/admin")
def admin():
    return render_template("admin.html")

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.join(base_dir, 'static'), filename)

if __name__ == "__main__":
    app.run(debug=True)