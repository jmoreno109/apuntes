
'''
from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
	return "hola mundo todos!"

#if __name__=='__main__':
#	app.run("localhost","8080",debug=True)
'''

'''
from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def inicio():
	return "pagina de inicio"

@app.route("/articulos")
def articulos():
	return "lista de articulos"

@app.route("/articulos/new",methods=["POST"])
def articulos_new():
	return "lista de articulos nuevos"

@app.route("/articulos/<int:id>")
def mostrar_articulos(id):
	return "El articulo a mostrar es: {}".format(id)

@app.route("/hola/")
@app.route("/hola/<string:nombre>")
@app.route("/hola/<string:nombre>/<int:edad>")
def hola(nombre=None,edad=None):
	if nombre and edad:
		return "hola {} tienes {} años".format(nombre,edad)
	elif nombre:
		return "hola {}".format(nombre)
	else:
		return "hola a todos"

@app.route("/login",methods=["GET","POST"])
def login():
	if request.method=='GET':
		return "peticion hecha con GET"
	elif request.method=='POST':
		return "peticion hecha con POST"
'''

'''
from flask import Flask,request
app=Flask(__name__)

@app.route('/info',methods=["GET","POST"])
def inicio():
    cad=""
    cad+="URL:"+request.url+"\n"
    cad+="Metodo:"+request.method+"\n"
    cad+="header:\n"
    for item,value in request.headers.items():
        cad+="{}:{}\n".format(item,value)
    cad+="informacion en formularios (POST):\n"
    for item,value in request.form.items():
        cad+="{}:{}\n".format(item,value)
    cad+="informacion en URL (GET):\n"
    for item,value in request.args.items():
        cad+="{}:{}\n".format(item,value)
    cad+="Ficheros:\n"
    for item,value in request.files.items():
        cad+="{}:{}\n".format(item,value)
    return cad

@app.route("/suma",methods=["GET","POST"])
def sumar():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		return str(int(num1)+int(num2))
	else:
		return <form action="/suma" method="POST">
				<label>N1:</label>
				<input type="text" name="num1"/>
				<label>N2:</label>
				<input type="text" name="num2"/>
                <input type="submit"/>
				</form>
'''

'''
from flask import Flask,make_response,abort,redirect,url_for
app=Flask(__name__)
@app.route('/string/')
def return_string():
    return 'Hello, world!'
@app.route('/object/')
def return_object():
    headers = {'Content-Type': 'text/plain'}
    return make_response('Hello, world!',200,headers)
@app.route('/tuple/')
def return_tuple():
    return 'Hello, world!',200, {'Content-Type':'text/plain'}
@app.route('/login')
def login():
	abort(401)
@app.errorhandler(404)
def page_not_found(error):
	return "pagina no encotrada",str(error)
@app.route("/")
def index():
	return redirect(url_for("return_string"))
@app.route('/salida')
def salida():
	response=make_response("hola a todos",200)
	response.headers["Content-Type"]="text/plain"
	return response
'''

'''
from flask import Flask,url_for
app=Flask(__name__)
@app.route('/')
def inicio():
    return '<img src="'+url_for('static', filename='img/tux.png')+'"/>'
'''

'''
from flask import Flask,jsonify,request
app=Flask(__name__)

@app.route("/app/v1/users",methods=["GET"])
def get_users():
	response={"msg":"get_users"}
	return jsonify(response)

@app.route("/app/v1/users/<id>",methods=["GET"])
def get_user(id):
	response={"msg":id}
	return jsonify(response)

@app.route("/app/v1/users",methods=["POST"])
def create_user():
	#param=request.form.get("id") # form-data
	json=request.get_json(force=True) # json
	param=json.get('id')
	print(param)
	response={"msg_create_user":param}
	return jsonify(response)

@app.route("/app/v1/users/<id>",methods=["PUT"])
def update_user(id):
	response={"msg_update_user":id}
	return jsonify(response)
	
@app.route("/app/v1/users/<id>",methods=["DELETE"])
def delete_user(id):
	response={"msg_delete_user":id}
	return jsonify(response)
'''

'''
from jinja2 import Template
temp7=
<ul>
{% for elem in elems -%}
<li>{{loop.index}} - {{ elem }}</li>
{% endfor -%}
</ul>
print(Template(temp7).render(elems=["amarillo","verde","rojo"]))
temp9=
{% if elems %}
<ul>
{% for elem in elems -%}
    {% if elem is divisibleby 2 -%}
        <li>{{elem}} es divisible por 2.</li>
    {% else -%}
        <li>{{elem}} no es divisible por 2.</li>
    {% endif -%}
{% endfor -%}
</ul>
{% endif %}
print(Template(temp9).render(elems=[1,2,3,4]))
'''

'''
from flask import Flask,render_template,abort
from flask_bootstrap import Bootstrap
app=Flask(__name__)
Bootstrap(app)
@app.route("/hola/")
@app.route("/hola/<nombre>",methods=["GET"])
def saluda(nombre=None):
	return render_template("template1.html",nombre=nombre)
@app.route("/suma/<num1>/<num2>")
def suma(num1,num2):
	try:
		resultado=int(num1)+int(num2)
	except:
		abort(404)
	return render_template("template2.html",num1=num1,num2=num2,resultado=resultado)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html",error="Página no encontrada..."),404
@app.route('/tabla/<numero>')
def tabla(numero):
    try:
        numero=int(numero)
    except:
        abort(404)
    return render_template("template3.html",num=numero)
'''

'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/formulario')
def formulario():
    return render_template("formulario.html")

@app.route("/procesar", methods=["post"])
def procesar_formulario():
	passwd=request.form.get("pass_control")
	if passwd=="asdasd":
		datos = request.form
		return render_template("datos.html",datos=datos)	
	else:
		return render_template("error.html",error="Contraseña incorrecta")

@app.route("/calculadora_post", methods=["get","post"])
def calculadora_post():
	if request.method=="POST":
		num1=request.form.get("num1")
		num2=request.form.get("num2")
		operador=request.form.get("operador")	
		try:
			resultado=eval(num1+operador+num2)
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		return render_template("calculadora_post.html")	

@app.route("/calculadora_get", methods=["get"])
def calculadora_get():
	if request.method=="GET" and len(request.args)>0:
		num1=request.args.get("num1")
		num2=request.args.get("num2")
		operador=request.args.get("operador")	
		try:
			resultado=eval(num1+operador+num2)
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)	
	else:
		return render_template("calculadora_get.html")	

@app.route("/calculadora/<operador>/<num1>/<num2>", methods=["get"])
def calculadora_var(operador,num1,num2):
	try:
		resultado=eval(num1+operador+num2)
	except:
			return render_template("error.html",error="No puedo realizar la operación")
	return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404
'''

'''
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from aplicacion.forms import formcalculadora
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():
    return render_template("inicio2.html")

@app.route("/calculadora_post", methods=["get","post"])
def calculadora_post():
	form=formcalculadora(request.form)
	if ( request.method=='POST' and form.validate_on_submit() ):
		num1=form.num1.data
		num2=form.num2.data
		operador=form.operador.data
		try:
			resultado=eval(str(num1)+operador+str(num2))
		except:
			return render_template("error.html",error="No puedo realizar la operación")
		return render_template("resultado.html",num1=num1,num2=num2,operador=operador,resultado=resultado)
	else:
		return render_template("calculadora_post2.html",form=form)
'''

'''
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from os import listdir
from aplicacion.forms import UploadForm
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
Bootstrap(app)	

@app.route('/')
def inicio():	
	lista=[]
	for file in listdir(app.root_path+"/static/img"):
		lista.append(file)
	print(lista)
	return render_template("inicio3.html",lista=lista)

@app.route('/upload', methods=['get', 'post'])
def upload():
	form= UploadForm() # carga request.from y request.file
	if request.method=='POST' and form.validate_on_submit():
		f = form.photo.data
		filename = secure_filename(f.filename)
		f.save(app.root_path+"/static/img/"+filename)
		return redirect(url_for('inicio'))
	return render_template('upload.html', form=form)	

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."),404
'''

'''
from flask import Flask, render_template,redirect,url_for,request,abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import *
from werkzeug.utils import secure_filename
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
import os

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from aplicacion.models import Articulos,Categorias,Usuarios
#from aplicacion.login import login_user,logout_user,is_login,is_admin

@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
	categoria=Categorias.query.get(id)
	if id=='0':
		articulos=Articulos.query.all()
	else:
		articulos=Articulos.query.filter_by(CategoriaId=id)
	categorias=Categorias.query.all()
	return render_template("inicio.html",articulos=articulos,categorias=categorias,categoria=categoria)

@app.route('/categorias')
def categorias():
	categorias=Categorias.query.all()
	return render_template("categorias.html",categorias=categorias)

@app.route('/categorias/new', methods=["get","post"])
def categorias_new():
	# Control de permisos
	print(is_admin())
	if not is_admin():
		abort(404)

	form=formCategoria(request.form)
	if form.validate_on_submit():
		cat=Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect(url_for("categorias"))
	else:
		return render_template("categorias_new.html",form=form)

@app.route('/categorias/<id>/edit', methods=["get","post"])
def categorias_edit(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)

	form=formCategoria(request.form,obj=cat)
		
	if form.validate_on_submit():
		form.populate_obj(cat)
		db.session.commit()
		return redirect(url_for("categorias"))

@app.route('/categorias/<id>/delete', methods=["get","post"])
def categorias_delete(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)
	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(cat)
			db.session.commit()
		return redirect(url_for("categorias"))
	return render_template("categorias_delete.html",form=form,cat=cat)

@app.route('/articulos/new', methods=["get","post"])
def articulos_new():
	# Control de permisos
	if not is_admin():
		abort(404)

	form=formArticulo()
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	if form.validate_on_submit():
		try:
			f = form.photo.data
			nombre_fichero=secure_filename(f.filename)
			f.save(app.root_path+"/static/upload/"+nombre_fichero)
		except:
			nombre_fichero=""
		art=Articulos()
		form.populate_obj(art)
		art.image=nombre_fichero
		db.session.add(art)
		db.session.commit()
		return redirect(url_for("inicio"))
	else:
		return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/edit', methods=["get","post"])
def articulos_edit(id):
	# Control de permisos
	if not is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formArticulo(obj=art)
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	
	if form.validate_on_submit():
		#Borramos la imagen anterior si hemos subido una nueva
		if  form.photo.data:
			os.remove(app.root_path+"/static/upload/"+art.image)
			try:
				f = form.photo.data
				nombre_fichero=secure_filename(f.filename)
				f.save(app.root_path+"/static/upload/"+nombre_fichero)
			except:
				nombre_fichero=""
		else:
			nombre_fichero=art.image
			
		form.populate_obj(art)
		art.image=nombre_fichero
		db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/delete', methods=["get","post"])
def articulos_delete(id):
		# Control de permisos
	if not is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			if art.image!="":
				os.remove(app.root_path+"/static/upload/"+art.image)
			db.session.delete(art)
			db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_delete.html",form=form,art=art)


@app.route('/login', methods=['get', 'post'])
def login():
	# Control de permisos
	if is_login():
		return redirect(url_for("inicio"))

	form = LoginForm()
	if form.validate_on_submit():
		user=Usuarios.query.filter_by(username=form.username.data).first()
		if user!=None and user.verify_password(form.password.data):
			login_user(user)
			return redirect(url_for('inicio'))
		form.username.errors.append("Usuario o contraseña incorrectas.")
	return render_template('login.html', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/registro",methods=["get","post"])
def registro():
	# Control de permisos
	if is_login():
		return redirect(url_for("inicio"))

	form=formUsuario()
	if form.validate_on_submit():
		existe_usuario=Usuarios.query.filter_by(username=form.username.data).first()
		if existe_usuario==None:
			user=Usuarios()
			form.populate_obj(user)
			user.admin=False
			db.session.add(user)
			db.session.commit()
			return redirect(url_for("inicio"))
		form.username.errors.append("Nombre de usuario ya existe.")
	return render_template("usuarios_new.html",form=form)

@app.route('/perfil/<username>', methods=["get","post"])
def perfil(username):
	# Control de permisos
	if not is_login():
		abort(404)
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formUsuario(request.form,obj=user)
	del form.password	
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("usuarios_new.html",form=form,perfil=True)

@app.route('/changepassword/<username>', methods=["get","post"])
def changepassword(username):
	# Control de permisos
	if not is_login():
		abort(404)
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formChangePassword()
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("changepassword.html",form=form)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404
'''

from flask import Flask, render_template,redirect,url_for,request,abort,session,make_response
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from aplicacion import config
from aplicacion.forms import formCategoria,formArticulo,formSINO,LoginForm,formUsuario,formChangePassword,formCarrito
from werkzeug.utils import secure_filename
from flask_login import LoginManager,login_user,logout_user,login_required,current_user
import os
import json

app = Flask(__name__)
app.config.from_object(config)
Bootstrap(app)	
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from aplicacion.models import Articulos,Categorias,Usuarios

@app.route('/')
@app.route('/categoria/<id>')
def inicio(id='0'):
	categoria=Categorias.query.get(id)
	if id=='0':
		articulos=Articulos.query.all()
	else:
		articulos=Articulos.query.filter_by(CategoriaId=id)
	categorias=Categorias.query.all()
	return render_template("inicio.html",articulos=articulos,categorias=categorias,categoria=categoria)

@app.route('/categorias')
def categorias():
	categorias=Categorias.query.all()
	return render_template("categorias.html",categorias=categorias)

@app.route('/categorias/new', methods=["get","post"])
@login_required
def categorias_new():
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	form=formCategoria(request.form)
	if form.validate_on_submit():
		cat=Categorias(nombre=form.nombre.data)
		db.session.add(cat)
		db.session.commit()
		return redirect(url_for("categorias"))
	else:
		return render_template("categorias_new.html",form=form)

@app.route('/categorias/<id>/edit', methods=["get","post"])
@login_required
def categorias_edit(id):
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)

	form=formCategoria(request.form,obj=cat)
		
	if form.validate_on_submit():
		form.populate_obj(cat)
		db.session.commit()
		return redirect(url_for("categorias"))
	
	return render_template("categorias_new.html",form=form)

@app.route('/categorias/<id>/delete', methods=["get","post"])
@login_required
def categorias_delete(id):
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	cat=Categorias.query.get(id)
	if cat is None:
		abort(404)
	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			db.session.delete(cat)
			db.session.commit()
		return redirect(url_for("categorias"))
	return render_template("categorias_delete.html",form=form,cat=cat)

@app.route('/articulos/new', methods=["get","post"])
@login_required
def articulos_new():
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	form=formArticulo()
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	if form.validate_on_submit():
		try:
			f = form.photo.data
			nombre_fichero=secure_filename(f.filename)
			f.save(app.root_path+"/static/upload/"+nombre_fichero)
		except:
			nombre_fichero=""
		art=Articulos()
		form.populate_obj(art)
		art.image=nombre_fichero
		db.session.add(art)
		db.session.commit()
		return redirect(url_for("inicio"))
	else:
		return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/edit', methods=["get","post"])
@login_required
def articulos_edit(id):
	# Control de permisos
	if not current_user.is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formArticulo(obj=art)
	categorias=[(c.id, c.nombre) for c in Categorias.query.all()[1:]]
	form.CategoriaId.choices = categorias
	
	if form.validate_on_submit():
		#Borramos la imagen anterior si hemos subido una nueva
		if  form.photo.data:
			os.remove(app.root_path+"/static/upload/"+art.image)
			try:
				f = form.photo.data
				nombre_fichero=secure_filename(f.filename)
				f.save(app.root_path+"/static/upload/"+nombre_fichero)
			except:
				nombre_fichero=""
		else:
			nombre_fichero=art.image
			
		form.populate_obj(art)
		art.image=nombre_fichero
		db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_new.html",form=form)

@app.route('/articulos/<id>/delete', methods=["get","post"])
@login_required
def articulos_delete(id):
		# Control de permisos
	if not current_user.is_admin():
		abort(404)

	art=Articulos.query.get(id)
	if art is None:
		abort(404)

	form=formSINO()
	if form.validate_on_submit():
		if form.si.data:
			if art.image!="":
				os.remove(app.root_path+"/static/upload/"+art.image)
			db.session.delete(art)
			db.session.commit()
		return redirect(url_for("inicio"))
	return render_template("articulos_delete.html",form=form,art=art)


@app.route('/login', methods=['get', 'post'])
def login():
	# Control de permisos
	if current_user.is_authenticated:
		return redirect(url_for("inicio"))

	form = LoginForm()
	if form.validate_on_submit():
		user=Usuarios.query.filter_by(username=form.username.data).first()
		if user!=None and user.verify_password(form.password.data):
			login_user(user)
			next = request.args.get('next')

			#if not is_safe_url(next):
			#	return abort(400)

			return redirect(next or url_for('inicio'))
		form.username.errors.append("Usuario o contraseña incorrectas.")
	return render_template('login.html', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route("/registro",methods=["get","post"])
def registro():
	# Control de permisos
	if current_user.is_authenticated:
		return redirect(url_for("inicio"))

	form=formUsuario()
	if form.validate_on_submit():
		existe_usuario=Usuarios.query.filter_by(username=form.username.data).first()
		if existe_usuario==None:
			user=Usuarios()
			form.populate_obj(user)
			user.admin=False
			db.session.add(user)
			db.session.commit()
			return redirect(url_for("inicio"))
		form.username.errors.append("Nombre de usuario ya existe.")
	return render_template("usuarios_new.html",form=form)

@app.route('/perfil/<username>', methods=["get","post"])
@login_required
def perfil(username):
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formUsuario(request.form,obj=user)
	del form.password	
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("usuarios_new.html",form=form,perfil=True)

@app.route('/changepassword/<username>', methods=["get","post"])
@login_required
def changepassword(username):
	user=Usuarios.query.filter_by(username=username).first()
	if user is None:
		abort(404)

	form=formChangePassword()
	if form.validate_on_submit():
		form.populate_obj(user)
		db.session.commit()
		return redirect(url_for("inicio"))

	return render_template("changepassword.html",form=form)

@login_manager.user_loader
def load_user(user_id):
	return Usuarios.query.get(int(user_id))


@app.route('/carrito/add/<id>',methods=["get","post"])
@login_required
def carrito_add(id):
	art=Articulos.query.get(id)	
	form=formCarrito()
	form.id.data=id
	if form.validate_on_submit():
		if art.stock>=int(form.cantidad.data):
			try:
				datos = json.loads(request.cookies.get(str(current_user.id)))
			except:
				datos = []
			actualizar= False
			for dato in datos:
				if dato["id"]==id:
					dato["cantidad"]=form.cantidad.data
					actualizar = True
			if not actualizar:
				datos.append({"id":form.id.data,"cantidad":form.cantidad.data})
			resp = make_response(redirect(url_for('inicio')))
			resp.set_cookie(str(current_user.id),json.dumps(datos))
			return resp
		form.cantidad.errors.append("No hay artículos suficientes.")
	return render_template("carrito_add.html",form=form,art=art)

@app.route('/carrito')
@login_required
def carrito():
	try:
		datos = json.loads(request.cookies.get(str(current_user.id)))
	except:
		datos = []
	articulos=[]
	cantidades=[]
	total=0
	for articulo in datos:
		articulos.append(Articulos.query.get(articulo["id"]))
		cantidades.append(articulo["cantidad"])
		total=total+Articulos.query.get(articulo["id"]).precio_final()*articulo["cantidad"]
	articulos=zip(articulos,cantidades)
	return render_template("carrito.html",articulos=articulos,total=total)

@app.route('/carrito_delete/<id>')
@login_required
def carrito_delete(id):
	try:
		datos = json.loads(request.cookies.get(str(current_user.id)))
	except:
		datos = []
	new_datos=[]
	for dato in datos:
		if dato["id"]!=id:
			new_datos.append(dato)
	resp = make_response(redirect(url_for('carrito')))
	resp.set_cookie(str(current_user.id),json.dumps(new_datos))
	return resp

@app.context_processor
def contar_carrito():
	if not current_user.is_authenticated:
		return {'num_articulos':0}
	if request.cookies.get(str(current_user.id))==None:
		return {'num_articulos':0}
	else:
		datos = json.loads(request.cookies.get(str(current_user.id)))
		return {'num_articulos':len(datos)}

@app.route('/pedido')
@login_required
def pedido():
    try:
        datos = json.loads(request.cookies.get(str(current_user.id)))
    except:
        datos = []
    total=0
    for articulo in datos:
        total=total+Articulos.query.get(articulo["id"]).precio_final()*articulo["cantidad"]
        Articulos.query.get(articulo["id"]).stock-=articulo["cantidad"]
        db.session.commit()
    resp = make_response(render_template("pedido.html",total=total))
    resp.set_cookie(str(current_user.id),"",expires=0)
    return resp

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error.html",error="Página no encontrada..."), 404