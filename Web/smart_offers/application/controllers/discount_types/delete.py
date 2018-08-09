import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_discount_type, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_discount_type) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_discount_type, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_discount_type) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_discount_type, **k):

    @staticmethod
    def POST_DELETE(id_discount_type, **k):
    '''

    def GET(self, id_discount_type, **k):
        message = None # Error message
        id_discount_type = config.check_secure_val(str(id_discount_type)) # HMAC id_discount_type validate
        result = config.model.get_discount_types(int(id_discount_type)) # search  id_discount_type
        result.id_discount_type = config.make_secure_val(str(result.id_discount_type)) # apply HMAC for id_discount_type
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_discount_type, **k):
        form = config.web.input() # get form data
        form['id_discount_type'] = config.check_secure_val(str(form['id_discount_type'])) # HMAC id_discount_type validate
        result = config.model.delete_discount_types(form['id_discount_type']) # get discount_types data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_discount_type = config.check_secure_val(str(id_discount_type))  # HMAC user validate
            id_discount_type = config.check_secure_val(str(id_discount_type))  # HMAC user validate
            result = config.model.get_discount_types(int(id_discount_type)) # get id_discount_type data
            result.id_discount_type = config.make_secure_val(str(result.id_discount_type)) # apply HMAC to id_discount_type
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/discount_types') # render discount_types delete.html 
