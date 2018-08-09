import web
import config

db = config.db


def get_all_companies():
    try:
        return db.select('companies')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_companies(id_company):
    try:
        return db.select('companies', where='id_company=$id_company', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_companies(id_company):
    try:
        return db.delete('companies', where='id_company=$id_company', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_companies(name,description,owner,type,address,created):
    try:
        return db.insert('companies',name=name,
description=description,
owner=owner,
type=type,
address=address,
created=created)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_companies(id_company,name,description,owner,type,address,created):
    try:
        return db.update('companies',id_company=id_company,
name=name,
description=description,
owner=owner,
type=type,
address=address,
created=created,
                  where='id_company=$id_company',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
