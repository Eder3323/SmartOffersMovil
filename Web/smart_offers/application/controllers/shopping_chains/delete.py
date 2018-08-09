import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_shopping_chain, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_shopping_chain) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_shopping_chain, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_shopping_chain) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_shopping_chain, **k):

    @staticmethod
    def POST_DELETE(id_shopping_chain, **k):
    '''

    def GET(self, id_shopping_chain, **k):
        message = None # Error message
        id_shopping_chain = config.check_secure_val(str(id_shopping_chain)) # HMAC id_shopping_chain validate
        result = config.model.get_shopping_chains(int(id_shopping_chain)) # search  id_shopping_chain
        result.id_shopping_chain = config.make_secure_val(str(result.id_shopping_chain)) # apply HMAC for id_shopping_chain
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_shopping_chain, **k):
        form = config.web.input() # get form data
        form['id_shopping_chain'] = config.check_secure_val(str(form['id_shopping_chain'])) # HMAC id_shopping_chain validate
        result = config.model.delete_shopping_chains(form['id_shopping_chain']) # get shopping_chains data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_shopping_chain = config.check_secure_val(str(id_shopping_chain))  # HMAC user validate
            id_shopping_chain = config.check_secure_val(str(id_shopping_chain))  # HMAC user validate
            result = config.model.get_shopping_chains(int(id_shopping_chain)) # get id_shopping_chain data
            result.id_shopping_chain = config.make_secure_val(str(result.id_shopping_chain)) # apply HMAC to id_shopping_chain
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/shopping_chains') # render shopping_chains delete.html 
