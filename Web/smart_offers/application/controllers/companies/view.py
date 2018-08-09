import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_company):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_company) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_company):
    '''

    def GET(self, id_company):
        id_company = config.check_secure_val(str(id_company)) # HMAC id_company validate
        result = config.model.get_companies(id_company) # search for the id_company data
        return config.render.view(result) # render view.html with id_company data
