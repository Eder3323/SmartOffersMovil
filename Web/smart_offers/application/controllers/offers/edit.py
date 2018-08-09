import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_offer, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_offer) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_offer, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_offer) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_offer, **k):

    @staticmethod
    def POST_EDIT(id_offer, **k):
        
    '''

    def GET(self, id_offer, **k):
        message = None # Error message
        id_offer = config.check_secure_val(str(id_offer)) # HMAC id_offer validate
        result = config.model.get_offers(int(id_offer)) # search for the id_offer
        result.id_offer = config.make_secure_val(str(result.id_offer)) # apply HMAC for id_offer
        return config.render.edit(result, message) # render offers edit.html

    def POST(self, id_offer, **k):
        form = config.web.input()  # get form data
        form['id_offer'] = config.check_secure_val(str(form['id_offer'])) # HMAC id_offer validate
        # edit user with new data
        result = config.model.edit_offers(
            form['id_offer'],form['name'],form['description'],form['creator'],form['product_name'],form['price'],form['discount_value'],form['new_price'],form['created'],
        )
        if result == None: # Error on udpate data
            id_offer = config.check_secure_val(str(id_offer)) # validate HMAC id_offer
            result = config.model.get_offers(int(id_offer)) # search for id_offer data
            result.id_offer = config.make_secure_val(str(result.id_offer)) # apply HMAC to id_offer
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/offers') # render offers index.html
