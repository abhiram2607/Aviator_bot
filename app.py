
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def extract_multipliers(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        multipliers = [float(x.replace('x', '').strip()) for x in text.split() if 'x' in x]
        return multipliers[-10:]
    except:
        return []

def predict_next(crash_data):
    if not crash_data:
        return "⚠️ No valid crash data found.", False
    high_crashes = [x for x in crash_data if x >= 4.0]
    low_since_last_high = 0
    for x in reversed(crash_data):
        if x >= 4.0:
            break
        low_since_last_high += 1
    if low_since_last_high >= 6:
        return "🟢 4x+ likely soon! Bet cautiously.", True
    elif low_since_last_high >= 4:
        return "🟡 Watch closely. 4x may appear in a few rounds.", False
    else:
        return "🔴 No strong signals for 4x yet.", False

def generate_plot(data):
    fig, ax = plt.subplots()
    ax.plot(range(len(data)), data, marker='o')
    ax.axhline(y=4.0, color='r', linestyle='--', label='4x Threshold')
    ax.set_title('Recent Crash Multipliers')
    ax.set_xlabel('Round')
    ax.set_ylabel('Multiplier (X)')
    ax.legend()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'screenshot' not in request.files:
            return redirect(request.url)
        file = request.files['screenshot']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            crash_data = extract_multipliers(filepath)
            prediction, alert = predict_next(crash_data)
            plot_url = generate_plot(crash_data) if crash_data else None
            return render_template('index.html', filename=filename, crash_data=crash_data, prediction=prediction, plot_url=plot_url)
    return render_template('index.html')
