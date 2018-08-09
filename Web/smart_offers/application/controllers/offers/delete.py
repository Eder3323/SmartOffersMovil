import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_offer, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_offer) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_offer, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_offer) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_offer, **k):

    @staticmethod
    def POST_DELETE(id_offer, **k):
    '''

    def GET(self, id_offer, **k):
        message = None # Error message
        id_offer = config.check_secure_val(str(id_offer)) # HMAC id_offer validate
        result = config.model.get_offers(int(id_offer)) # search  id_offer
        result.id_offer = config.make_secure_val(str(result.id_offer)) # apply HMAC for id_offer
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_offer, **k):
        form = config.web.input() # get form data
        form['id_offer'] = config.check_secure_val(str(form['id_offer'])) # HMAC id_offer validate
        result = config.model.delete_offers(form['id_offer']) # get offers data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_offer = config.check_secure_val(str(id_offer))  # HMAC user validate
            id_offer = config.check_secure_val(str(id_offer))  # HMAC user validate
            result = config.model.get_offers(int(id_offer)) # get id_offer data
            result.id_offer = config.make_secure_val(str(result.id_offer)) # apply HMAC to id_offer
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/offers') # render offers delete.html 
