import sqlite3


#
# class Connection:
#     res = []
#
#     def __init__(self):
#         self.uniq_obj = []
#         self.uniq_prod = []
#         self.uniq_vol = []
#         self.connection_to_db()
#         self.choose_object()
#
#     def connection_to_db(self):
#         with sqlite3.connect('database/database.db') as db:
#             cursor = db.cursor()
#             query = "SELECT * FROM Лист1"
#             cursor.execute(query)
#             self.res = cursor.fetchall()
#
#         return self.res
#
#     def choose_object(self):
#         for objects in self.res:
#             if objects[2] not in self.uniq_obj:
#                 self.uniq_obj.append(objects[2])
#         return self.uniq_obj
#
#     def choose_product(self, type_object):
#         for product in self.res:
#             if product[4] not in self.uniq_prod:
#                 self.uniq_prod.append(product[4])
#         if type_object == "Резервуар":
#             return [self.uniq_prod[0], self.uniq_prod[1]]
#         elif type_object == "Трубопровод":
#             return [self.uniq_prod[1], self.uniq_prod[3]]
#
#     def choose_volume(self, type_object):
#         for vol in self.res:
#             if vol[3] not in self.uniq_vol:
#                 self.uniq_vol.append(vol[3])
#         if type_object == "Нефть":
#
#             return [self.uniq_vol[0], self.uniq_vol[1], self.uniq_vol[2]]
#         elif type_object == "Нефтепродукт":
#             return [self.uniq_vol[3], self.uniq_vol[4], self.uniq_vol[5], self.uniq_vol[6], self.uniq_vol[7],
#                     self.uniq_vol[8], self.uniq_vol[9]]
#
#
class Connection:
    def connection_to_db(self):
        return


class ConnectionObject(Connection):
    def __init__(self):
        Connection.__init__(self)
        self.res = []

    def connection_to_db(self, type_object):
        with sqlite3.connect('database/dataset.db') as db:
            cursor = db.cursor()
            params = (type_object,)
            query = "SELECT * FROM dataset WHERE Type_of_object = ?;"
            cursor.execute(query, params)
            self.res = cursor.fetchall()

        return self.res
