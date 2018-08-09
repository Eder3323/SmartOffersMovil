import web
import config

db = config.db


def get_all_shopping_chains():
    try:
        return db.select('shopping_chains')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_shopping_chains(id_shopping_chain):
    try:
        return db.select('shopping_chains', where='id_shopping_chain=$id_shopping_chain', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_shopping_chains(id_shopping_chain):
    try:
        return db.delete('shopping_chains', where='id_shopping_chain=$id_shopping_chain', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_shopping_chains(client,offer,status,creator,limited_time,created):
    try:
        return db.insert('shopping_chains',client=client,
offer=offer,
status=status,
creator=creator,
limited_time=limited_time,
created=created)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_shopping_chains(id_shopping_chain,client,offer,status,creator,limited_time,created):
    try:
        return db.update('shopping_chains',id_shopping_chain=id_shopping_chain,
client=client,
offer=offer,
status=status,
creator=creator,
limited_time=limited_time,
created=created,
                  where='id_shopping_chain=$id_shopping_chain',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
