#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
nom = form.getvalue('nom')
prenom  = form.getvalue('prenom')
age = form.getvalue('age')
pseudo = form.getvalue('pseudo')

def verifUnique(nom,prenom,age,pseudo):
    f = open('db','r')
    lineAjoute = nom+";"+prenom+";"+pseudo+";"+age
    for line in f:
        if (line == lineAjoute):
            return (False)


print ("""Content-type:text/html\r\n\r\n
<html>
    <head>
        <title>Confirmation</title>
        <meta http-equiv='content-type' content='text/html;charset=UTF-8'>
        <link rel="stylesheet" href="css/bootstrap.min.css">
    </head>
    <body>
    
    <div class="row">
        <div class="container-fluid col-10">
        <h1>Bienvenu !</h1>
            <h2>Bonjour %s %s, A.K.A %s</h2>
            <p>Vous avez %s ans</p>
               <div class="row">
                   <form action="users.py">
                        <div class="form-group col-6">
                            <button type="submit" value="Jettertest un coup d'oeil aux utilisateurs" class="btn btn-primary">Jetter un oeil aux utilisateurs</button>
                        </div>
                    </form>
                </div>
                
            </form>

        </div>
        </div>
    </body>
</html>"""% (prenom, nom,pseudo,age))
