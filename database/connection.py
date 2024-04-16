import sqlite3


class Connection:
    res = []

    def __init__(self):
        self.uniq_obj = []
        self.uniq_prod = []
        self.connection_to_db()
        self.choose_object()
        # self.choose_product()

    def connection_to_db(self):
        with sqlite3.connect('database/database.db') as db:
            cursor = db.cursor()
            query = "SELECT * FROM Лист1"
            cursor.execute(query)
            self.res = cursor.fetchall()

        return self.res

    def choose_object(self):
        for objects in self.res:
            if objects[2] not in self.uniq_obj:
                self.uniq_obj.append(objects[2])
        return self.uniq_obj

    def choose_product(self, object):
        for product in self.res:
            if product[4] not in self.uniq_prod:
                self.uniq_prod.append(product[4])
        if object == "Резервуар":
            return [self.uniq_prod[0], self.uniq_prod[1]]
        elif object == "Трубопровод":
            return [self.uniq_prod[1], self.uniq_prod[3]]
