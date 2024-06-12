
from models.__init__ import CURSOR, CONN

class Station:
    all = {}
    def __init__(self, station_name, id=None):
        self.id=id
        self.station_name = station_name

    def __repr__(self):
        return (
            f"<Station {self.id}: {self.station_name}>"
        )

    @property
    def station_name(self):
        return self._station_name

    @station_name.setter
    def station_name(self, station_name):
        if isinstance(station_name, str) and len(station_name) > 0:
            self._station_name = station_name
        else:
            raise ValueError(
                "Station name must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Station instances """
        sql = """
            CREATE TABLE IF NOT EXISTS stations (
            id INTEGER PRIMARY KEY,
            station_name TEXT NOT NULL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Station instances """
        sql = """
            DROP TABLE IF EXISTS stations;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with station name values of the current Station object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's Primary Key as dictionary key"""
        sql = """
                INSERT INTO stations (station_name)
                VALUES (?)
        """

        CURSOR.execute(sql, (self.station_name,))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Station instance."""
        sql = """
            UPDATE stations 
            SET station_name = ? 
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.station_name, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Station instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM stations
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    # def delete(self):
    #     """Delete the table row corresponding to the current Station instance,
    #     delete the dictionary entry, and reassign id attribute"""

    #     sql = """
    #         DELETE FROM stations
    #         WHERE id = ?
    #     """

    #     CURSOR.execute(sql, (self.id,))
    #     CONN.commit()

    #     # Delete the dictionary entry using id as the key
    #     del type(self).all[self.id]

    #     # Set the id to None
    #     self.id = None

    @classmethod
    def create(cls, station_name):
        """ Initialize a new Station instance and save the object to the database """
        station = cls(station_name)
        station.save()
        return station

    @classmethod
    def instance_from_db(cls, row):
        """Return an Station object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        station = cls.all.get(row[0])
        if station:
            # ensure attributes match row values in case local instance was modified
            station.station_name = row[1]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            station = cls(row[1],)
            station.id = row[0]
            cls.all[station.id] = station
        return station

    @classmethod
    def get_all(cls):
        """Return a list containing one Station object per table row"""
        sql = """
            SELECT *
            FROM stations
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Station object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM stations 
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return Station object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM stations
            WHERE station_name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
