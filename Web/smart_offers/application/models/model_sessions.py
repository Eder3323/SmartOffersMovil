import web
import config

db = config.db


def get_all_sessions():
    try:
        return db.select('sessions')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_sessions(session_id):
    try:
        return db.select('sessions', where='session_id=$session_id', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_sessions(session_id):
    try:
        return db.delete('sessions', where='session_id=$session_id', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_sessions(atime,data):
    try:
        return db.insert('sessions',atime=atime,
data=data)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_sessions(session_id,atime,data):
    try:
        return db.update('sessions',session_id=session_id,
atime=atime,
data=data,
                  where='session_id=$session_id',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
