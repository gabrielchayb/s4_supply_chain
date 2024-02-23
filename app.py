from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#Iniciando a aplicação flask
app = Flask(__name__)
app.secret_key = 'minha senha secreta'

#conectando ao banco de dados MySql - fiz utilizando php my admin/wamp server, mas funciona no workbench também
app.config['MYSQL_HOST'] = 'localhost'#o banco roda apenas no localhost
app.config['MYSQL_USER'] = 'root' #usuario padrão, se você tiver um usuário insira aqui
app.config['MYSQL_PASSWORD'] = '' #sua senha, se você tiver uma insira aqui 
app.config['MYSQL_DB'] = 'crudapplication' #nome do seu banco de dados

mysql = MySQL(app) 


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM product") #aqui acessamos a tabela product que está dentro do banco de dados crudapplication
    data = cur.fetchall()
    cur.close()

    return render_template('index2.html', product=data ) 



@app.route('/insert', methods = ['POST']) #primeiro metodo: inserir dados do produto
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully") #flash = mensagem em forma de pop up apenas para direcionar o usuario que a inserção na tabela funcionou
        name = request.form['name'] 
        description = request.form['description']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO product (name, description, price) VALUES (%s, %s, %s)", (name, description, price)) #rodando SQL para inserir as informações do produto na tabela
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET']) #segundo metodo: deletar um produto baseado no seu id
def delete(id_data):
    flash("Record Has Been Deleted Successfully") 
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM product WHERE id=%s", (id_data,)) #rodando SQL para deletar, com base no id, as informações do produto na tabela
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update',methods=['POST','GET']) #terceiro metodo: atualizar/editar um produto
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        cur = mysql.connection.cursor()
        cur.execute(""" 
               UPDATE product
               SET name=%s, description=%s, price=%s
               WHERE id=%s
            """, (name, description, price, id_data)) #rodando SQL para atualizar as informações do produto na tabela
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))
    
if __name__ == "__main__":
     app.run(debug=True)

     #proximas versões: implementar RESTapi, implementar sistema de login