from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista kontaktów w pamięci programu
contacts = [
    {"name": "John Doe", "phone": "123456789"},
    {"name": "Jane Smith", "phone": "987654321"},
    {"name": "Alice Johnson", "phone": "555555555"}
]

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']
    if len(phone) != 9 or not phone.isdigit():
        return "Invalid phone number! Phone number must be 9 digits long."
    new_contact = Contact(name, phone)
    contacts.append({"name": new_contact.name, "phone": new_contact.phone})
    return redirect('/')

@app.route('/delete_contact/<name>', methods=['GET'])
def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'] != name]
    return redirect('/')

@app.route('/edit_contact/<name>', methods=['GET', 'POST'])
def edit_contact(name):
    if request.method == 'GET':
        contact = next((contact for contact in contacts if contact['name'] == name), None)
        if contact:
            return render_template('edit_contact.html', contact=contact)
        else:
            return "Contact not found."
    elif request.method == 'POST':
        new_name = request.form['name']
        new_phone = request.form['phone']
        if len(new_phone) != 9 or not new_phone.isdigit():
            return "Invalid phone number! Phone number must be 9 digits long."
        for contact in contacts:
            if contact['name'] == name:
                contact['name'] = new_name
                contact['phone'] = new_phone
                break
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
