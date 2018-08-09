import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_company, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_company) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_company, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_company) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_company, **k):

    @staticmethod
    def POST_EDIT(id_company, **k):
        
    '''

    def GET(self, id_company, **k):
        message = None # Error message
        id_company = config.check_secure_val(str(id_company)) # HMAC id_company validate
        result = config.model.get_companies(int(id_company)) # search for the id_company
        result.id_company = config.make_secure_val(str(result.id_company)) # apply HMAC for id_company
        return config.render.edit(result, message) # render companies edit.html

    def POST(self, id_company, **k):
        form = config.web.input()  # get form data
        form['id_company'] = config.check_secure_val(str(form['id_company'])) # HMAC id_company validate
        # edit user with new data
        result = config.model.edit_companies(
            form['id_company'],form['name'],form['description'],form['owner'],form['type'],form['address'],form['created'],
        )
        if result == None: # Error on udpate data
            id_company = config.check_secure_val(str(id_company)) # validate HMAC id_company
            result = config.model.get_companies(int(id_company)) # search for id_company data
            result.id_company = config.make_secure_val(str(result.id_company)) # apply HMAC to id_company
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/companies') # render companies index.html
