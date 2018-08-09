import web
import config

db = config.db


def get_all_company_types():
    try:
        return db.select('company_types')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_company_types(id_company_types):
    try:
        return db.select('company_types', where='id_company_types=$id_company_types', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_company_types(id_company_types):
    try:
        return db.delete('company_types', where='id_company_types=$id_company_types', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_company_types(name,description,created):
    try:
        return db.insert('company_types',name=name,
description=description,
created=created)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_company_types(id_company_types,name,description,created):
    try:
        return db.update('company_types',id_company_types=id_company_types,
name=name,
description=description,
created=created,
                  where='id_company_types=$id_company_types',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
