import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_company_types, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_company_types) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_company_types, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_company_types) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_company_types, **k):

    @staticmethod
    def POST_DELETE(id_company_types, **k):
    '''

    def GET(self, id_company_types, **k):
        message = None # Error message
        id_company_types = config.check_secure_val(str(id_company_types)) # HMAC id_company_types validate
        result = config.model.get_company_types(int(id_company_types)) # search  id_company_types
        result.id_company_types = config.make_secure_val(str(result.id_company_types)) # apply HMAC for id_company_types
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_company_types, **k):
        form = config.web.input() # get form data
        form['id_company_types'] = config.check_secure_val(str(form['id_company_types'])) # HMAC id_company_types validate
        result = config.model.delete_company_types(form['id_company_types']) # get company_types data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_company_types = config.check_secure_val(str(id_company_types))  # HMAC user validate
            id_company_types = config.check_secure_val(str(id_company_types))  # HMAC user validate
            result = config.model.get_company_types(int(id_company_types)) # get id_company_types data
            result.id_company_types = config.make_secure_val(str(result.id_company_types)) # apply HMAC to id_company_types
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/company_types') # render company_types delete.html 
