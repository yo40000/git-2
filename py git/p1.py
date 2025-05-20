#para agregar nuevos cambios, se pone git add mas el nombre del archivo
#despues pones commit y se guarda commit -m con el nombre de el mesaje entre
#comillas  git log muestra los cambios hechos, git status muestra si hay 
#algun archivo modificado para guardar git commit -a guarda los cambios 
#sin seleccionar el archivo  git log --graph muestra el progreso de la rama
# graficamente 
#git alias crear un alias git config --global alias. nombre del alias seguido de las funciones ejmeplo --graph etc
# git ignore se crea .gitignore se crea con el comando touch .gitignore dentro se ponen los archivos que se 
# van a ignorar con el sigiente codigo dentro delarchivo **/.nombre del archivo 
#git diff muestra las diferencias en el archivo
#crear una nueva rama con git branch mas el nombre de la rama
#cambiar de rama git switch mas el nombre de la rama a la que se quiere ir
#para conbinar dos ramas diferentes se utiliza el comando git merge crea un 
# commit si no hay conficto las ramas se conbinan 
#para guadar cambios en los que seguiras trabajando despues
#se utiliza el comando git stash no hace un commit pero guada los comabios
#git stash list lista los cambios temporales, git stash drop para eliminar temporales  
#para recuperar los cambiso temporales se usa git stash pop
#eliminacion de ramas git branch -d nombre de la rama 
#ve cambios entre las ramas git diff (nombre de la rama)
print("holas")
print("adios")

num1=55
num2=55

print (num1 + num2)
print (num1 - num2)
print (num1 * num2)
print (num1 / num2)

print("hola amigos") 