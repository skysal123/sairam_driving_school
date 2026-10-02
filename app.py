import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sairam_driving_school_secret"

# --- Configuration / Placeholders ---
CONFIG = {
    "business_name": "SAIRAM DRIVING SCHOOL",
    "tagline": "Learn to Drive. Drive with Confidence.",
    "phone": "+91 9689512652",
    "whatsapp": "919689512652",
    "email": "sairamdrivingschool@gmail.com",
    "address": "Survey 43/1, Sai Plaza, Satav Vasti, Near Gulmohar City, Kharadi",
    "city": "Pune",
    "area": "Kharadi",
    "pincode": "411014",
    "google_maps_link": "https://www.google.com/maps/search/?api=1&query=Sairam+Driving+School+Kharadi+Pune+411014",
    "whatsapp_msg": "Hi Sairam Driving School, I would like to enquire about driving lessons."
}

# --- Routes ---

@app.route('/')
def home():
    return render_template('index.html', config=CONFIG)

@app.route('/about')
def about():
    return render_template('about.html', config=CONFIG)

@app.route('/courses')
def courses():
    return render_template('courses.html', config=CONFIG)

@app.route('/vehicles')
def vehicles():
    return render_template('vehicles.html', config=CONFIG)

@app.route('/contact')
def contact():
    return render_template('contact.html', config=CONFIG)

@app.route('/blog')
def blog_list():
    return render_template('blog/list.html', config=CONFIG)

@app.route('/blog/<slug>')
def blog_detail(slug):
    # Placeholder for blog content
    return render_template('blog/detail.html', config=CONFIG, slug=slug)

@app.route('/enquire', methods=['POST'])
def enquire():
    # Lead management logic would go here
    name = request.form.get('name')
    phone = request.form.get('phone')
    course = request.form.get('course')

    # For now, we just flash a success message
    flash(f"Thank you {name}! Your enquiry for {course} has been received. We will contact you shortly.")
    return redirect(url_for('contact'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
