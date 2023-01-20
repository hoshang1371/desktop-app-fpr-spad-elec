import pickle
import os

def storeData(EncryptedToken,key):
    # initializing data to be stored in db
    if os.path.exists("examplePickle"):
        os.remove("examplePickle")
    data = {'token' : EncryptedToken, 'key' : key,}
    # database
    # db = {}
    # db['dataToken'] = data
      
    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')
      
    # source, destination
    pickle.dump(data, dbfile)                     
    dbfile.close()

    os.system( "attrib +h examplePickle" )
  
def loadData():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')     
    db = pickle.load(dbfile)
    # for keys in db:
    #     print(keys, '=>', db[keys])
    dbfile.close()
    return db
 
if __name__ == '__main__':
    # if os.path.exists("examplePickle"):
    #     os.remove("examplePickle")
    # os.system( "attrib +h examplePickle" )
    # subprocess.check_call(["attrib","+H","examggplePickle.txt"])

    storeData()
    # os.system( "attrib +h examplePickle" )
    loadData()

    if os.path.exists("examplePickle"):
        os.remove("examplePickle")
        print("exist")