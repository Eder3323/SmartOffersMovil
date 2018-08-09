import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_company, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_company) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_company, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_company) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_company, **k):

    @staticmethod
    def POST_DELETE(id_company, **k):
    '''

    def GET(self, id_company, **k):
        message = None # Error message
        id_company = config.check_secure_val(str(id_company)) # HMAC id_company validate
        result = config.model.get_companies(int(id_company)) # search  id_company
        result.id_company = config.make_secure_val(str(result.id_company)) # apply HMAC for id_company
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_company, **k):
        form = config.web.input() # get form data
        form['id_company'] = config.check_secure_val(str(form['id_company'])) # HMAC id_company validate
        result = config.model.delete_companies(form['id_company']) # get companies data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_company = config.check_secure_val(str(id_company))  # HMAC user validate
            id_company = config.check_secure_val(str(id_company))  # HMAC user validate
            result = config.model.get_companies(int(id_company)) # get id_company data
            result.id_company = config.make_secure_val(str(result.id_company)) # apply HMAC to id_company
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/companies') # render companies delete.html 
