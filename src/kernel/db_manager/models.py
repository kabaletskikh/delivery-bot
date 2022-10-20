from abc import ABCMeta, abstractmethod


class Model():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get():
        """Получить объект"""

    @abstractmethod
    def set():
        """Изменить объект"""



class User(Model):
    def __init__(self, sql, form, sv):
        self.sv = sv
        self.db = sql
        self.form = form


    def get(self, user_id=False, user_tg_id=False):
        user = False

        if not (user_id == False):
            user = self.db.fetchBySign("users", "user_id", user_id)
    
        if not (user_tg_id == False):
            user = self.db.fetchBySign("users", "tg_id", user_tg_id)
        
        if not user:
            self.sv.trace("User model can't find user with id [" + user_id + "] tg_id [" + user_tg_id + "]", "DB Models")
            return False
        
        data = {
            "id": str(user[1]),
            "tg_id": str(user[2])
        }

        self.sv.trace("User model founded with id [" + user_id + "] tg_id [" + user_tg_id + "]: " + str(data), "DB Models")
        return data


    def set(self, user_id=False, user_tg_id=False, updated_phone=False):
        user = self.get(user_id, user_tg_id)

        if not user:
            return False
        
        if not (updated_phone == False):
            res = self.db.update_row("users", "user_id", user["id"], "user_phone", str(updated_phone))
            self.sv.trace("User model with id [" + user_id + "] tg_id [" + user_tg_id + "] updated with phone [" + updated_phone + "]", "DB Models")
            return res


    def new(self, tg_id):
        newid = self.db.fetchMaxId("users", "user_id")
        newid += 1
        self.db.create_new("users", (newid, tg_id))
        self.db.create_new("carts", (newid, "0"))
        self.db.create_new("favorites", (newid, "0"))
        self.sv.trace("User model with id [" + newid + "] tg_id [" + tg_id + "] created", "DB Models")




class Category(Model):
    def __init__(self, sql, form):
        self.db = sql
        self.form = form


    def get(self, category_id=False, category_name=False):
        category = False

        if not (category_id == False):
            category = self.db.fetchBySign("categoryes", "category_id", category_id)
        
        if not (category_name == False):
            category = self.db.fetchBySign("categoryes", "name", category_name)

        if not category:
            self.sv.trace("Category model can't find category with id [" + category_id + "] name [" + category_name + "]", "DB Models")
            return False

        data = {
            "id": str(category[1]),
            "name": str(category[2]),
            "description": str(category[3]),
            "image": str(category[4]),
            "products": self.form.string_to_list(category[5]),
            "subcategoryes": self.form.string_to_list(category[6])
        }

        self.sv.trace("Category model founded with id [" + category_id + "] name [" + category_name + "]: " + str(data), "DB Models")
        return data



class Product(Model):
    def __init__(self, sql, form):
        self.db = sql
        self.form = form


    def get(self, product_id=False, product_name=False):
        product = False

        if not (product_id == False):
            product = self.db.fetchBySign("products", "product_id", product_id)
        
        if not (product_name == False):
            product = self.db.fetchBySign("products", "name", product_name)

        if not product:
            self.sv.trace("Product model can't find product with id [" + product_id + "] name [" + product_name + "]", "DB Models")
            return False

        if str(product[4]) == "0":
            product[4] = None
        else:
            product[4] = "./images/" + str(product[4])

        data = {
            "id": str(product[1]),
            "name": str(product[2]),
            "description": str(product[3]),
            "image": str(product[4]),
            "price": str(product[5]),
            "is_over": str(product[6])
        }

        self.sv.trace("Product model founded with id [" + product_id + "] name [" + product_name + "]: " + str(data), "DB Models")
        return data



class Cart(Model):
    def __init__(self, sql, form):
        self.db = sql
        self.form = form


    def get(self, cart_id):
        cart = self.db.fetchBySign("carts", "user_id", cart_id)
        
        if not cart:
            self.sv.trace("Cart model can't find category cart id [" + cart_id + "]", "DB Models")
            return False

        data = {
            "id": str(cart[1]),
            "products": self.form.string_to_list(cart[2])
        }

        self.sv.trace("Cart model founded with id [" + cart_id + "]: " + str(data), "DB Models")
        return data


    def set(self, cart_id, data):
        if not self.get(cart_id):
            return False

        res = self.db.update_row("carts", "user_id", cart_id, "products", self.form.list_to_string(data))
        self.sv.trace("Cart model with id [" + cart_id + "] updated with [" + data + "]", "DB Models")
        return res




class Favorites(Model):
    def __init__(self, sql, form):
        self.db = sql
        self.form = form


    def get(self, favorites_id):
        fav = self.db.fetchBySign("cart", "favorites_id", favorites_id)

        if not fav:
            self.sv.trace("Favorites model can't find fav cart id [" + favorites_id + "]", "DB Models")
            return False

        data = {
            "id": str(fav[1]),
            "products": self.form.string_to_list(fav[2])
        }

        self.sv.trace("Favorites model founded with id [" + favorites_id + "]: " + str(data), "DB Models")
        return data


    def set(self, favorites_id, data):
        if not self.get(favorites_id):
            return False

        res = self.db.update_row("favorites", "user_id", favorites_id, "products", self.form.list_to_string(data))
        self.sv.trace("Favorites model with id [" + favorites_id + "] updated with [" + data + "]", "DB Models")
        return res



class DbModels():
    user
    category
    product
    cart
    favorites

    def __init__(self, sql_translator, form, sv):
        self.user = User(sql_translator, form, sv)
        self.sv.trace("Модуль успешно подключен", "DB Models")