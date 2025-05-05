from collections import defaultdict

produits = defaultdict(list, {1: [{'id_prod': 1, 'type': 'Smathphone', 'nom': 'Iphone', 'prix': 250, 'image': 'static/images/th_10.webp', 'desc': 'tsara dia tsara', 'nombre': 0}, {'id_prod': 1, 'type': 'Smathphone', 'nom': 'Iphone', 'prix': 250, 'image': 'static/images/th_10.webp', 'desc': 'tsara dia tsara', 'nombre': 1}, {'id_prod': 1, 'type': 'Smathphone', 'nom': 'Iphone', 'prix': 250, 'image': 'static/images/th_10.webp', 'desc': 'tsara dia tsara', 'nombre': 2}], 2: [{'id_prod': 2, 'type': 'smartphones', 'nom': 'Andoid', 'prix': 150, 'image': 'static/images/th_9.webp', 'desc': 'mora be', 'nombre': 3}], 3: [{'id_prod': 3, 'type': 'accessoirs', 'nom': 'souris', 'prix': 50, 'image': 'static/images/s3.webp', 'desc': 'vaovao', 'nombre': 4}]})

# print(produits.items())
for key,produit in produits.items():
    for prod in produit:
        print(prod["nom"])
        print(prod["id_prod"])
    