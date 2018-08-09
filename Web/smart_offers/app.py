# Author : Salvador Hernandez Mendoza
# Email  : salvadorhm@gmail.com
# Twitter: @salvadorhm
import web
import config


#activate ssl certificate
ssl = False

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    '/users', 'application.controllers.users.index.Index',
    '/users/printer', 'application.controllers.users.printer.Printer',
    '/users/view/(.+)', 'application.controllers.users.view.View',
    '/users/edit/(.+)', 'application.controllers.users.edit.Edit',
    '/users/delete/(.+)', 'application.controllers.users.delete.Delete',
    '/users/insert', 'application.controllers.users.insert.Insert',
    '/users/change_pwd', 'application.controllers.users.change_pwd.Change_pwd',
    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',
    '/companies', 'application.controllers.companies.index.Index',
    '/companies/view/(.+)', 'application.controllers.companies.view.View',
    '/companies/edit/(.+)', 'application.controllers.companies.edit.Edit',
    '/companies/delete/(.+)', 'application.controllers.companies.delete.Delete',
    '/companies/insert', 'application.controllers.companies.insert.Insert',
    '/company_types', 'application.controllers.company_types.index.Index',
    '/company_types/view/(.+)', 'application.controllers.company_types.view.View',
    '/company_types/edit/(.+)', 'application.controllers.company_types.edit.Edit',
    '/company_types/delete/(.+)', 'application.controllers.company_types.delete.Delete',
    '/company_types/insert', 'application.controllers.company_types.insert.Insert',
    '/discount_types', 'application.controllers.discount_types.index.Index',
    '/discount_types/view/(.+)', 'application.controllers.discount_types.view.View',
    '/discount_types/edit/(.+)', 'application.controllers.discount_types.edit.Edit',
    '/discount_types/delete/(.+)', 'application.controllers.discount_types.delete.Delete',
    '/discount_types/insert', 'application.controllers.discount_types.insert.Insert',
    '/offers', 'application.controllers.offers.index.Index',
    '/offers/view/(.+)', 'application.controllers.offers.view.View',
    '/offers/edit/(.+)', 'application.controllers.offers.edit.Edit',
    '/offers/delete/(.+)', 'application.controllers.offers.delete.Delete',
    '/offers/insert', 'application.controllers.offers.insert.Insert',
    '/shopping_chains', 'application.controllers.shopping_chains.index.Index',
    '/shopping_chains/view/(.+)', 'application.controllers.shopping_chains.view.View',
    '/shopping_chains/edit/(.+)', 'application.controllers.shopping_chains.edit.Edit',
    '/shopping_chains/delete/(.+)', 'application.controllers.shopping_chains.delete.Delete',
    '/shopping_chains/insert', 'application.controllers.shopping_chains.insert.Insert',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'kuorra'
    web.config.session_parameters['timeout'] = 10
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
