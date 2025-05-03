from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/light/minerals')
def minerals():
    return render_template('light/minerals.html')

@app.route('/light/ores')
def ores():
    return render_template('light/ores.html')

@app.route('/light/fossils')
def fossils():
    return render_template('light/fossils.html')

@app.route('/light/global_warming')
def global_warming():
    return render_template('light/global_warming.html')

@app.route('/dark/')
def index_d():
    return render_template('dark/.html')

@app.route('/dark/minerals')
def minerals_d():
    return render_template('dark/minerals.html')

@app.route('/dark/ores')
def ores_d():
    return render_template('dark/ores.html')

@app.route('/dark/fossils')
def fossils_d():
    return render_template('dark/fossils.html')

@app.route('/dark/global_warming')
def global_warming_d():
    return render_template('dark/global_warming.html')

if __name__ == '__main__':
    app.run(debug=True)