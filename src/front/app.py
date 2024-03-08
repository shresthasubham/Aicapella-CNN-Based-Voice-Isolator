from flask import Flask, render_template, request, flash, redirect, send_file
from vocal_isolator import extract_vocals
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(__file__)
uploads_file_path = os.path.join(BASE_DIR,'static/uploads/uploaded_song.wav')
outputs_file_path = os.path.join(BASE_DIR,'static/outputs/output_song.wav')
models_file_path =  os.path.join(BASE_DIR,'static/models/100model.keras')
@app.route('/', methods=['GET','POST'])
def index():
    processed_file = False
    if request.method == 'POST':


        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        

        uploaded_file = request.files['file']

        if uploaded_file.filename != '' and uploaded_file.filename.endswith('.wav'):
            # Save the file to a desired location
            
            uploaded_file.save(uploads_file_path)
            extract_vocals()
            #check()
            print(f"File saved at: {uploads_file_path}")
            processed_file = True
            #message = 'File processed successfully.'
            return render_template('index.html', processed_file = processed_file)
        else:
            return "Please upload a valid .wav file."
        

    return render_template('index.html')


@app.route('/download')
def download_file():
    file_path = outputs_file_path
    return send_file(file_path, as_attachment=True)

# @app.route('/upload', methods=['GET','POST'])
# def upload_file():
#     uploaded_file = request.files['file']

#     if uploaded_file.filename != '' and uploaded_file.filename.endswith('.wav'):
#         # Save the file to a desired location
#         file_path = "uploads/uploaded_song.wav"
#         uploaded_file.save(file_path)
#         extract_vocals()
#         #check()
#         print(f"File saved at: {file_path}")
#         return "File uploaded successfully."
#     else:
#         return "Please upload a valid .wav file."

if __name__ == "__main__":
    app.run(debug= True)