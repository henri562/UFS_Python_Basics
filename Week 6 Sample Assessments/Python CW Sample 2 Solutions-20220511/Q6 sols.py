
cats =['Lion', 'Tiger','Leopard']    
new_cat = input('Add a cat: ')

if new_cat not in cats:
    cats.append(new_cat)
    print(cats)
else:
     cats.remove(new_cat)
     print(cats)

