from app import app, photos

from flask import redirect, render_template, request, session, url_for
from process.FaceDetection import FaceDetection as FD
import os
import requests
#import cv2

# Upload model
#model = FD.upload_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    # set session for image results

    #if "file_urls" not in session:
    session['file_urls'] = []
    session['file_names'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']
    file_names = session['file_names']

    # handle image upload from Dropszone
    if request.method == 'POST': # Request handles the uploaded data
        file_obj = request.files   # Request.files object containing the uploaded files
                                    # it is a multidict obj
        #message = request.get_json(force=True)
        for f in file_obj:  
            # encoded = message['image']
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )

            # append image urls

            file_url = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], file.filename)
            file_urls.append(file_url)
            #file_urls.append(photos.url(filename))
            file_names.append(filename)

        session['file_urls'] = file_urls
        session['file_names'] = file_names
        return "uploading..."
    # return dropzone template on GET request
    return render_template('public/index.html')


@app.route('/results')
def results():
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))

    # set the file_urls and remove the session variable
    #print(session)
    file_urls = session['file_urls']
    file_names = session['file_names']
    inf_file_paths = []

    # # instatiate our classifier

    for i, file_url in enumerate(file_urls):

        # image_path = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], file_name)
        save_path = os.path.join(app.config['INFERRED_PHOTOS_DEST'], file_names[i])
        #image = FD.run_detection(model, file_url, save_path=save_path)
        image = FD.save_same_photo(file_url, save_path=save_path)
        inf_file_paths.append(os.path.join(app.config['INFERRED_PHOTOS_DEST'], file_names[i]))
 
    session.pop('file_urls', None)
    session.pop('file_names', None)
    session.pop('inf_file_paths', None)

    return render_template('public/results.html', file_names=file_names)


