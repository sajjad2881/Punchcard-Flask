from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rewards')
def rewards():
    return render_template('rewards.html')

@app.route('/business-dashboard')
def business_dashboard():
    return render_template('business-dashboard.html')

@app.route('/claim-code')
def claim_code():
    return render_template('claim-code.html')

@app.route('/explore-page')
def explore_page():
    return render_template('explore-page.html')

if __name__ == '__main__':
    app.run(debug=True)
