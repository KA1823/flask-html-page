import os
from flask import Flask, render_template, request

app=Flask(__name__,template_folder='template',
                    static_url_path='/',
                    static_folder='static'
                    )
app.config["IMAGE_UPLOADS"] = "/home/shahrukh/python-projects/flask-html-page/media"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            return render_template("upload.html", uploaded_image=image.filename)
    return render_template("upload.html")


@app.route('/static/IMG/<filename>')
def send_uploaded_file(filename=''):
    from flask import send_from_directory
    return send_from_directory(app.config["IMAGE_UPLOADS"], filename)

if __name__ == "__main__":
    app.run()