def save_recipes(request):
    file_name = 'db.txt'
    with open(file_name,"w",  encoding="utf-8") as file:
        file.write("Holii")
    return "Ok"