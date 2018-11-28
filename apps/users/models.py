from peewee import *
from bcrypt import hashpw, gensalt
from Form.models import BaseModel


class PasswordHash(bytes):
    def check_password(self, password):
        password = password.encode('utf-8')
        return hashpw(password, self) == self


class PasswordField(BlobField):
    def __init__(self, iterations=12, *args, **kwargs):
        if None in (hashpw, gensalt):
            raise ValueError('Missing library required for PasswordField: bcrypt')
        self.bcrypt_iterations = iterations
        self.raw_password = None
        super(PasswordField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        """Convert the python value for storage in the database."""
        if isinstance(value, PasswordHash):
            return bytes(value)

        if isinstance(value, str):
            value = value.encode('utf-8')
        salt = gensalt(self.bcrypt_iterations)
        return value if value is None else hashpw(value, salt)

    def python_value(self, value):
        """Convert the database value to a pythonic value."""
        if isinstance(value, str):
            value = value.encode('utf-8')
        return PasswordHash(value)


class User(BaseModel):
    GENDERS = (
        ("female", "女"),
        ("male", "男"),
    )
    mobile = CharField(verbose_name="手机号码", max_length=11, index=True, unique=True)
    password = PasswordField(verbose_name="密码")
    nick_name = CharField(verbose_name="昵称", max_length=20, null=True)
    head_url = CharField(verbose_name="头像", max_length=200, null=True)
    address = CharField(verbose_name="地址", max_length=200, null=True)
    desc = TextField(verbose_name="个人简介", null=True)
    gender = CharField(verbose_name="性别", max_length=200, choices=GENDERS, null=True)