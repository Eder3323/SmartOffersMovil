import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_shopping_chain, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_shopping_chain) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_shopping_chain, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_shopping_chain) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_shopping_chain, **k):

    @staticmethod
    def POST_EDIT(id_shopping_chain, **k):
        
    '''

    def GET(self, id_shopping_chain, **k):
        message = None # Error message
        id_shopping_chain = config.check_secure_val(str(id_shopping_chain)) # HMAC id_shopping_chain validate
        result = config.model.get_shopping_chains(int(id_shopping_chain)) # search for the id_shopping_chain
        result.id_shopping_chain = config.make_secure_val(str(result.id_shopping_chain)) # apply HMAC for id_shopping_chain
        return config.render.edit(result, message) # render shopping_chains edit.html

    def POST(self, id_shopping_chain, **k):
        form = config.web.input()  # get form data
        form['id_shopping_chain'] = config.check_secure_val(str(form['id_shopping_chain'])) # HMAC id_shopping_chain validate
        # edit user with new data
        result = config.model.edit_shopping_chains(
            form['id_shopping_chain'],form['client'],form['offer'],form['status'],form['creator'],form['limited_time'],form['created'],
        )
        if result == None: # Error on udpate data
            id_shopping_chain = config.check_secure_val(str(id_shopping_chain)) # validate HMAC id_shopping_chain
            result = config.model.get_shopping_chains(int(id_shopping_chain)) # search for id_shopping_chain data
            result.id_shopping_chain = config.make_secure_val(str(result.id_shopping_chain)) # apply HMAC to id_shopping_chain
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/shopping_chains') # render shopping_chains index.html
