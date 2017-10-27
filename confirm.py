#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
nom = form.getvalue('nom').lower()
prenom  = form.getvalue('prenom').lower()
age = form.getvalue('age').lower()
pseudo = form.getvalue('pseudo').lower()


def verifUnique(nom,prenom,age,pseudo):
    f = open('db','r')
    lineAjoute = nom+";"+prenom+";"+pseudo+";"+age
    for line in f:
        if (line == lineAjoute):
            f.close()
            return (False)
    f.close()
    return (True)


print ("""Content-type:text/html\r\n\r\n
<html>
    <head>
        <title>Confirmation</title>
        <meta http-equiv='content-type' content='text/html;charset=UTF-8'>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
    </head>
    <body>
    
    <div class="row">
        <div class="container-fluid col-10">""")
if (verifUnique(nom,prenom,age,pseudo)):
    f = open('db', 'a')
    f.write(nom + ";" + prenom + ";" + pseudo + ";" + age+"\n")
    f.close()
    print("""<h1>Bienvenu !</h1>
            <h2>Bonjour %s %s, A.K.A %s</h2>
            <p>Vous avez %s ans</p>
    """% (prenom.capitalize(), nom.capitalize(),pseudo.capitalize(),age))
else:
    print("""
    <h1 style="color:red;">Attention !</h1>
    <h2>Bonjour %s %s, A.K.A %s</h2>
    <p>Vous etes deja inscris dans la base de donnees !</p>
    """% (prenom.capitalize(), nom.capitalize(),pseudo.capitalize()))


print("""
<div class="row"> 
                   <form action="users.py"> 
                        <div class="form-group col-6"> 
                            <button type="submit" value="Jetter un coup d'oeil aux utilisateurs" class="btn btn-primary">Jetter un oeil aux utilisateurs</button> 
                        </div> 
                    </form> 
                </div> 
</div>    
        </div>
    </body>
     <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
</html>""")

