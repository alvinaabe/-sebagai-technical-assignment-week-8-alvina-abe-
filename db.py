dari  mengetik  impor  Koleksi
impor  pymongo
impor  uuid

klien  =  pymongo . MongoClient ( "mongodb+srv://gilang:cQxUZhoHw7SmyBfa@cluster0.lco38k5.mongodb.net/?retryWrites=true&w=majority" )
db  =  klien . basis data
koleksi  =  db . Gugus0

def  locationn ( kecepatan , lintang , bujur , stempel waktu ):
    data  = {
        "ID transaksi" : str ( uuid . uuid4 ()),
        "kecepatan" : 90 ,
        "lintang" : 6.2088 ,
        "bujur" : 106.8456
        " stempel waktu ": stempel waktu
    }
    catatan  =  koleksi . insert_one ( data )
    print ( "data tersimpan" , record )
