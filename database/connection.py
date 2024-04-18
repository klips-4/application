import sqlite3


class Connection:
    def connection_to_db(self, type_object):
        with sqlite3.connect('database/dataset.db') as db:
            cursor = db.cursor()
            params = (type_object,)
            query = "SELECT DISTINCT Type_of_product FROM dataset WHERE Type_of_object = ?"
            cursor.execute(query, params)
            self.res = cursor.fetchall()
            self.result = [item[0] for item in self.res]

        return self.result

    def get_filtered_volume(self, product_value, object_value):
        with sqlite3.connect('database/dataset.db') as db:
            cursor = db.cursor()
            params = (object_value, product_value, )
            query = "SELECT DISTINCT Diameter_or_volume FROM dataset WHERE Type_of_object = ? AND Type_of_product = ?"
            cursor.execute(query, params)
            self.res = cursor.fetchall()
            self.result = [item[0] for item in self.res]

        return self.result

    def get_filtered_methods(self, product_value, object_value):
        with sqlite3.connect('database/dataset.db') as db:
            cursor = db.cursor()
            params = (object_value, product_value, )
            query = "SELECT DISTINCT Construction_method FROM dataset WHERE Type_of_object = ? AND Diameter_or_volume = ?"
            cursor.execute(query, params)
            self.res = cursor.fetchall()
            self.result = [item[0] for item in self.res]

        return self.result


class ConnectionObject(Connection):

    def __init__(self):
        Connection.__init__(self)

    def get_uniq_products(self, type_object):
        self.type_of_object = type_object
        return super().connection_to_db(type_object)

    def get_uniq_volume(self, product_value, object_value):
        return super().get_filtered_volume(product_value, object_value)

    def get_uniq_method_construction(self, product_value, object_value):
        return super().get_filtered_methods(product_value, object_value)
