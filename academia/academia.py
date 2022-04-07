from flask import Flask, render_template, request, redirect

app: Flask = Flask(__name__)


class Alunos:
    def __init__(self, codigo, nome, ultimo_nome, idade, peso, altura):
        self._id = codigo
        self._nome = nome
        self._ultimo_nome = ultimo_nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def ultimo_nome(self):
        return self._ultimo_nome

    @property
    def idade(self):
        return self._idade

    @property
    def peso(self):
        return self._peso

    @property
    def altura(self):
        return self._altura

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @ultimo_nome.setter
    def ultimo_nome(self, ultimo_nome):
        self._ultimo_nome = ultimo_nome

    @peso.setter
    def peso(self, peso):
        self._peso = peso

    @altura.setter
    def altura(self, altura):
        self._altura = altura


aluno1 = Alunos(1, 'Gabriel', 'Malachias', 27, 85.6, 1.75)
aluno2 = Alunos(2, 'Ariane', 'Malachias', 32, 69.5, 1.65)
aluno3 = Alunos(3, 'Filipe', 'Reis', 31, 79.5, 1.85)
lista = [aluno1, aluno2, aluno3]


@app.route("/")
def alunos():
    return render_template('alunos.html', titulo='lista de Alunos', alunos=lista)


@app.route("/novoaluno")
def novo():
    return render_template('novoaluno.html')


@app.route("/cadastro", methods=['POST'])
def cadastro():
    codigo = request.form['id']
    nome = request.form['nome']
    ultimo_nome = request.form['ultimo_nome']
    idade = request.form['idade']
    peso = request.form['peso']
    altura = request.form['altura']
    aluno = Alunos(codigo, nome, ultimo_nome, idade, peso, altura)
    lista.append(aluno)
    return redirect("/")


@app.route("/alterar")
def alterar():
    return render_template('alteraluno.html', titulo='Alterar dados')

app.run(debug=True)
