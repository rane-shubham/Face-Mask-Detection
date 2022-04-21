from flask import Flask, render_template, Response
from mask_detect_video_app import VideoCamera
from flask import send_file

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


@app.route('/about_us')
def about_us():
    """ About Me page"""
    return render_template('about_us.html')


def gen(camera, start):
    """Video streaming generator function."""
    if start==True:
        while True:
            frame = camera.get_frame()
            yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(VideoCamera(), True),mimetype='multipart/x-mixed-replace; boundary=frame')
                 
if __name__ == "__main__":
    app.run(debug=True)
                 