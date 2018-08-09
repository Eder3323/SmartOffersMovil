import web
import config

db = config.db


def get_all_offers():
    try:
        return db.select('offers')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_offers(id_offer):
    try:
        return db.select('offers', where='id_offer=$id_offer', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_offers(id_offer):
    try:
        return db.delete('offers', where='id_offer=$id_offer', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_offers(name,description,creator,product_name,price,discount_value,new_price,created):
    try:
        return db.insert('offers',name=name,
description=description,
creator=creator,
product_name=product_name,
price=price,
discount_value=discount_value,
new_price=new_price,
created=created)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_offers(id_offer,name,description,creator,product_name,price,discount_value,new_price,created):
    try:
        return db.update('offers',id_offer=id_offer,
name=name,
description=description,
creator=creator,
product_name=product_name,
price=price,
discount_value=discount_value,
new_price=new_price,
created=created,
                  where='id_offer=$id_offer',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
