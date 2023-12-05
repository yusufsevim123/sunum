from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')




# Diğer route'lar buraya gelecek

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # İletişim formu gönderildiğinde burası çalışacak
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        return render_template("contact.html",name=name ,email=email,message=message)
    else:
        return render_template("contact.html")

@app.route('/store', methods=['GET', 'POST'])
def store():
    return render_template("store.html")
        # Burada iletişim formu verilerini kullanarak istediğiniz işlemleri yapabilirsiniz
        
@app.route('/submit-contact', methods=['GET', 'POST'])
def submit_contact():
    return render_template("store.html")
        # Burada iletişim formu verilerini kullanarak istediğiniz işlemleri yapabilirsiniz
        
    

if __name__ == '__main__':
     app.run(debug=True)


