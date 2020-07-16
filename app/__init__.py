from flask import Flask
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class

import os

app = Flask(__name__)
dropzone = Dropzone(app)


app.config['SECRET_KEY'] = 'supersecretkeygoeshere'


# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = True
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results' # where we are redirected in cas of dropzon

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '\\app\\static\\img\\uploads'
app.config['INFERRED_PHOTOS_DEST'] = os.getcwd() + '\\app\\static\\img\\inferred'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


from app import views
