import web
import config

db = config.db


def get_all_logs():
    try:
        return db.select('logs')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_logs(id_log):
    try:
        return db.select('logs', where='id_log=$id_log', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_logs(id_log):
    try:
        return db.delete('logs', where='id_log=$id_log', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_logs(username,ip,access):
    try:
        return db.insert('logs',username=username,
ip=ip,
access=access)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_logs(id_log,username,ip,access):
    try:
        return db.update('logs',id_log=id_log,
username=username,
ip=ip,
access=access,
                  where='id_log=$id_log',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
