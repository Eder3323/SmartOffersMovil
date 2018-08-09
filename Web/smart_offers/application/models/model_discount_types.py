import web
import config

db = config.db


def get_all_discount_types():
    try:
        return db.select('discount_types')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_discount_types(id_discount_type):
    try:
        return db.select('discount_types', where='id_discount_type=$id_discount_type', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_discount_types(id_discount_type):
    try:
        return db.delete('discount_types', where='id_discount_type=$id_discount_type', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_discount_types(name,description,value,created):
    try:
        return db.insert('discount_types',name=name,
description=description,
value=value,
created=created)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_discount_types(id_discount_type,name,description,value,created):
    try:
        return db.update('discount_types',id_discount_type=id_discount_type,
name=name,
description=description,
value=value,
created=created,
                  where='id_discount_type=$id_discount_type',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
