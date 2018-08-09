import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, session_id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(session_id) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, session_id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(session_id) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(session_id, **k):

    @staticmethod
    def POST_DELETE(session_id, **k):
    '''

    def GET(self, session_id, **k):
        message = None # Error message
        session_id = config.check_secure_val(str(session_id)) # HMAC session_id validate
        result = config.model.get_sessions(int(session_id)) # search  session_id
        result.session_id = config.make_secure_val(str(result.session_id)) # apply HMAC for session_id
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, session_id, **k):
        form = config.web.input() # get form data
        form['session_id'] = config.check_secure_val(str(form['session_id'])) # HMAC session_id validate
        result = config.model.delete_sessions(form['session_id']) # get sessions data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            session_id = config.check_secure_val(str(session_id))  # HMAC user validate
            session_id = config.check_secure_val(str(session_id))  # HMAC user validate
            result = config.model.get_sessions(int(session_id)) # get session_id data
            result.session_id = config.make_secure_val(str(result.session_id)) # apply HMAC to session_id
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/sessions') # render sessions delete.html 
