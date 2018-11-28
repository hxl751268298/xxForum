from tornado import web, ioloop

from peewee_async import Manager

from Form.urls import urlpatterns
from Form.settings import settings, database


if __name__ == "__main__":
    #集成json到wtforms
    import wtforms_json
    wtforms_json.init()
    app = web.Application(urlpatterns, debug=True, **settings)
    app.listen(8888)

    objects = Manager(database)
    database.set_allow_sync(False)

    app.objects = objects
    ioloop.IOLoop.current().start()

