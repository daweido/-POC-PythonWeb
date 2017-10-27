#!/usr/bin/python
# coding=utf-8
print ("""Content-type:text/html\r\n\r\n
<html>
    <head>
        <title>Welcome</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
                <link rel="shortcut icon" href="img/logo.png">
    </head>
    <body>
        <body>
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="./index.py">POC</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link" href="./index.py">Accueil<span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="./users.py">Utilisateurs</a>
      </li>
    </ul>
  </div>
</nav>
<div class="container-fluid">
<h1>Bienvenu dans notre POC</h1>
    <div class="row">
        <div class="container-fluid col-6">
            <form action="confirm.py" method="get">
                <div class="row">
                    <div class="form-group col-6">
                        <label for="prenom">Prenom :</label>
                        <input type="text" class="form-control" id="prenom" name="prenom" placeholder="Prenom">
                    </div>
    
                    <div class="form-group col-6">
                        <label for="nom">Nom :</label>
                        <input type="text" class="form-control" id="nom" name="nom" placeholder="Nom">
                    </div>
               
                </div>
                 <div class="row">
                 <div class="form-group col-6">
                        <label for="pseudo">Pseudo :</label>
                        <input type="text" class="form-control" id="pseudo" name="pseudo" placeholder="Pseudo">
                    </div>
                 
                <div class="form-group col-4">
                    <label for="age">Age :</label>
                    <input type="text" class="form-control" id="age" name="age" placeholder="Age">
                </div>
                </div>
               <div class="row">
                <div class="form-group col-6">
                    <button type="submit" value="submit" class="btn btn-primary">Submit</button>
                </div>
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
