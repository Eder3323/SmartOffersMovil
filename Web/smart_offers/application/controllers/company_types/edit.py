import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_company_types, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_company_types) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_company_types, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_company_types) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_company_types, **k):

    @staticmethod
    def POST_EDIT(id_company_types, **k):
        
    '''

    def GET(self, id_company_types, **k):
        message = None # Error message
        id_company_types = config.check_secure_val(str(id_company_types)) # HMAC id_company_types validate
        result = config.model.get_company_types(int(id_company_types)) # search for the id_company_types
        result.id_company_types = config.make_secure_val(str(result.id_company_types)) # apply HMAC for id_company_types
        return config.render.edit(result, message) # render company_types edit.html

    def POST(self, id_company_types, **k):
        form = config.web.input()  # get form data
        form['id_company_types'] = config.check_secure_val(str(form['id_company_types'])) # HMAC id_company_types validate
        # edit user with new data
        result = config.model.edit_company_types(
            form['id_company_types'],form['name'],form['description'],form['created'],
        )
        if result == None: # Error on udpate data
            id_company_types = config.check_secure_val(str(id_company_types)) # validate HMAC id_company_types
            result = config.model.get_company_types(int(id_company_types)) # search for id_company_types data
            result.id_company_types = config.make_secure_val(str(result.id_company_types)) # apply HMAC to id_company_types
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/company_types') # render company_types index.html
