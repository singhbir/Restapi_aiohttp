"""
THIS MODULE CONTAIN TABLES OF DB AND THIER FIELDS
"""
from datetime import datetime
import peewee


db = peewee.SqliteDatabase("test.db")


class Agent(peewee.Model):
    """
    AGENT TABLE IN DATABASE WITH FIELDS uuid,agentdate,agentip
    """

    uuid = peewee.CharField(primary_key=True)
    agentdate = peewee.DateTimeField(default=datetime.utcnow)
    agentip = peewee.CharField()

    class Meta:
        """
        META CLASS FOR INFO ABOUT DB AND TABLE
        """
        database = db
        db_table = "agent"


class System(peewee.Model):
    """
    SYSTEM TABLE IN DB WITH FIELDS sysname,sid
    """

    agent = peewee.ForeignKeyField(Agent, backref='systems')
    sysname = peewee.CharField()
    sid = peewee.CharField()

    class Meta:
        """
        META CLASS FOR INFO ABOUT DB AND TABLE
        """
        database = db
        db_table = "system"



Agent.create_table()
System.create_table()
