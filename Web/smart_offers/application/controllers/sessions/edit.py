import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, session_id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(session_id) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, session_id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(session_id) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(session_id, **k):

    @staticmethod
    def POST_EDIT(session_id, **k):
        
    '''

    def GET(self, session_id, **k):
        message = None # Error message
        session_id = config.check_secure_val(str(session_id)) # HMAC session_id validate
        result = config.model.get_sessions(int(session_id)) # search for the session_id
        result.session_id = config.make_secure_val(str(result.session_id)) # apply HMAC for session_id
        return config.render.edit(result, message) # render sessions edit.html

    def POST(self, session_id, **k):
        form = config.web.input()  # get form data
        form['session_id'] = config.check_secure_val(str(form['session_id'])) # HMAC session_id validate
        # edit user with new data
        result = config.model.edit_sessions(
            form['session_id'],form['atime'],form['data'],
        )
        if result == None: # Error on udpate data
            session_id = config.check_secure_val(str(session_id)) # validate HMAC session_id
            result = config.model.get_sessions(int(session_id)) # search for session_id data
            result.session_id = config.make_secure_val(str(result.session_id)) # apply HMAC to session_id
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/sessions') # render sessions index.html
