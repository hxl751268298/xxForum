from peewee import MySQLDatabase

from apps.users.models import User
from apps.community.models import CommunityGroup, CommunityGroupMember
from Form.settings import database


database = MySQLDatabase(
    'forum', host="127.0.0.1", port=3306, user="root", password="123456"
)

def init():
    #生成表
    database.create_tables([User])
    database.create_tables([CommunityGroup, CommunityGroupMember])


if __name__=="__main__":
    init()