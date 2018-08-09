import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, id_company_types):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(id_company_types) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_company_types):
    '''

    def GET(self, id_company_types):
        id_company_types = config.check_secure_val(str(id_company_types)) # HMAC id_company_types validate
        result = config.model.get_company_types(id_company_types) # search for the id_company_types data
        return config.render.view(result) # render view.html with id_company_types data
