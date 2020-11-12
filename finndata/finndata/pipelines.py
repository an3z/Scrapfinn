from sqlalchemy.orm import sessionmaker
from .models import finnboligDB, db_connect, create_table, NewboligDB, ParkingDB

class FinndataPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        finnbolig = finnboligDB()


        try:
            finnbolig.finn_code = item['finn_code']
            finnbolig.address = item['address']
            finnbolig.total_price = item['total_price']
            finnbolig.common_costs = item['common_costs']
            finnbolig.for_sale_price = item['for_sale_price']
            finnbolig.ownership_form = item['ownership_form']
            finnbolig.building_type = item['building_type']
            finnbolig.bedrooms = item['bedrooms']
            finnbolig.pra = item['pra']
            finnbolig.year_built = item['year_built']
            finnbolig.last_changed = item['last_changed']
            finnbolig.rooms = item['rooms']
        except Exception as e:
            print(e)

        try:
            session.add(finnbolig)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

class NewFinndataPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        newboligDB = NewboligDB()

        try:
            newboligDB.finn_code = item['finn_code']
            newboligDB.address = item['address']
            newboligDB.total_price = item['total_price']
            newboligDB.common_costs = item['common_costs']
            newboligDB.for_sale_price = item['for_sale_price']
            newboligDB.bedrooms = item['bedrooms']
            newboligDB.pra = item['pra']
            newboligDB.last_changed = item['last_changed']
            newboligDB.rooms = item['rooms']
        except Exception as e:
            print(e)

        try:
            session.add(newboligDB)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item

class parkingPipeline(object):

    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates deals table.
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)


    def process_item(self, item, spider):
        """Save deals in the database.

        This method is called for every item pipeline component.
        """
        session = self.Session()
        parkingDB = ParkingDB()

        try:
            parkingDB.finn_code = item['finn_code']
            parkingDB.address = item['address']
            parkingDB.headline = item['headline']
            parkingDB.title = item['title']
            parkingDB.price = item['price']
            parkingDB.timestamp = item['timestamp']
        except Exception as e:
            print(e)

        try:
            session.add(parkingDB)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item