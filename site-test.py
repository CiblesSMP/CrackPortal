from flask import Flask, send_from_directory

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/CrackPortal/")
def serve_index():
    return send_from_directory(".", "index.html")

@app.route("/CrackPortal/<path:filename>")
def serve_file(filename):
    return send_from_directory(".", filename)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5080, debug=True)