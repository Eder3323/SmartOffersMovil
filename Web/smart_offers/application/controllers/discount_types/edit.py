import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_discount_type, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_discount_type) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_discount_type, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_discount_type) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_discount_type, **k):

    @staticmethod
    def POST_EDIT(id_discount_type, **k):
        
    '''

    def GET(self, id_discount_type, **k):
        message = None # Error message
        id_discount_type = config.check_secure_val(str(id_discount_type)) # HMAC id_discount_type validate
        result = config.model.get_discount_types(int(id_discount_type)) # search for the id_discount_type
        result.id_discount_type = config.make_secure_val(str(result.id_discount_type)) # apply HMAC for id_discount_type
        return config.render.edit(result, message) # render discount_types edit.html

    def POST(self, id_discount_type, **k):
        form = config.web.input()  # get form data
        form['id_discount_type'] = config.check_secure_val(str(form['id_discount_type'])) # HMAC id_discount_type validate
        # edit user with new data
        result = config.model.edit_discount_types(
            form['id_discount_type'],form['name'],form['description'],form['value'],form['created'],
        )
        if result == None: # Error on udpate data
            id_discount_type = config.check_secure_val(str(id_discount_type)) # validate HMAC id_discount_type
            result = config.model.get_discount_types(int(id_discount_type)) # search for id_discount_type data
            result.id_discount_type = config.make_secure_val(str(result.id_discount_type)) # apply HMAC to id_discount_type
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/discount_types') # render discount_types index.html
