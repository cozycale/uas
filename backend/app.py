from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
import json 


#Create an instance of Flask
app = Flask(__name__)

#Create an instance of MySQL
mysql = MySQL()

#Create an instance of Flask RESTful API
api = Api(app)

#Set database credentials in config.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'uas_21450410028'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#Initialize the MySQL extension
mysql.init_app(app)


#Get All Users, or Create a new user
class ListPembeli(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from pembeli""")
            rows = cursor.fetchall()
            json_rows = [dict(zip(('nama_pembeli', 'jk', 'no_tlp', 'alamat', 'id_pembeli'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nama_pembeli = request.form['nama_pembeli']
            _jk = request.form['jk']
            _no_tlp = request.form['no_tlp']
            _alamat = request.form['alamat']
            insert_pembeli_cmd = """INSERT INTO pembeli(nama_pembeli, jk, no_tlp, alamat) 
                                VALUES(%s, %s, %s, %s)"""
            cursor.execute(insert_pembeli_cmd, (_nama_pembeli, _jk, _no_tlp, _alamat))
            conn.commit()
            response = jsonify(message='Pembeli added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add pembeli.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user
class Pembeli(Resource):
    def get(self, id_pembeli):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from pembeli where id_pembeli = %s',id_pembeli)
            rows = cursor.fetchall()
            json_rows = [dict(zip(('nama_pembeli', 'jk', 'no_tlp', 'alamat', 'id_pembeli'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, id_pembeli):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nama_pembeli = request.form['nama_pembeli']
            _jk = request.form['jk']
            _no_telp = request.form['no_telp']
            _alamat = request.form['alamat']
            update_pembeli_cmd = """update pembeli 
                                 set nama_pembeli=%s, jk=%s, no_telp=%s alamat=%s
                                 where id_pembeli=%s"""
            cursor.execute(update_pembeli_cmd, (_nama_pembeli, _jk, _no_telp, _alamat, id_pembeli))
            conn.commit()
            response = jsonify('Pembeli updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update pembeli.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, id_pembeli):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from pembeli where id_pembeli = %s',id_pembeli)
            conn.commit()
            response = jsonify('Pembeli deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete barang.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)  

class ListBarang(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from barang""")
            rows = cursor.fetchall()
            json_rows = [dict(zip(('nama_barang', 'harga', 'stok', 'id_barang'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nama_barang = request.form['nama_barang']
            _harga = request.form['harga']
            _stok = request.form['stok']
            insert_barang_cmd = """INSERT INTO barang(nama_barang, harga, stok) 
                                VALUES(%s, %s, %s)"""
            cursor.execute(insert_barang_cmd, (_nama_barang, _harga, _stok))
            conn.commit()
            response = jsonify(message='Barang added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add barang.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user
class Barang(Resource):
    def get(self, id_barang):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from barang where id_barang = %s',id_barang)
            rows = cursor.fetchall()
            json_rows = [dict(zip(('nama_barang', 'harga', 'stok', 'id_barang'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, id_barang):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _nama_barang = request.form['nama_barang']
            _harga = request.form['harga']
            _stok = request.form['stok']
            update_barang_cmd = """update barang 
                                 set nama_barang=%s, harga=%s, stok=%s
                                 where id_barang=%s"""
            cursor.execute(update_barang_cmd, (_nama_barang, _harga, _stok, id_barang))
            conn.commit()
            response = jsonify('Barang updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update barang.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, id_barang):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from barang where id_barang = %s',id_barang)
            conn.commit()
            response = jsonify('Barang deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete barang.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

class ListTransaksi(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""select * from transaksi""")
            rows = cursor.fetchall()
            json_rows = [dict(zip(('id_transaksi', 'id_barang', 'id_pembeli', 'tanggal', 'keterangan'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _id_barang = request.form['id_barang']
            _id_pembeli = request.form['id_pembeli']
            _tanggal = request.form['tanggal']
            _keterangan   = request.form['keterangan']
            insert_barang_cmd = """INSERT INTO transaksi(id_barang, id_pembeli, tanggal, keterangan) 
                                VALUES(%s, %s, %s, %s)"""
            cursor.execute(insert_barang_cmd, (_id_barang, _id_pembeli, _tanggal, _keterangan) )
            conn.commit()
            response = jsonify(message='transaksi added successfully.', id=cursor.lastrowid)
            #response.data = cursor.lastrowid
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add transaksi.')         
            response.status_code = 400 
        finally:
            cursor.close()
            conn.close()
            return(response)
            
#Get a user by id, update or delete user
class Transaksi(Resource):
    def get(self, id_transaksi):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('select * from transaksi where id_transaksi = %s',id_transaksi)
            rows = cursor.fetchall()
            json_rows = [dict(zip(('id_transaksi', 'id_barang', 'id_pembeli', 'tanggal', 'keterangan'), (str(key), *values))) for key, *values in rows]
            return jsonify(json_rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def put(self, id_transaksi):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _id_barang = request.form['id_barang']
            _id_pembeli = request.form['id_pembeli']
            _tanggal = request.form['tanggal']
            _keterangan = request.form['keterangan']
            update_transaksi_cmd = """update transaksi 
                                 set id_barang=%s, id_pembeli=%s, tanggal=%s, keterangan=%s
                                 where id_transaksi=%s"""
            cursor.execute(update_transaksi_cmd, (_id_barang, _id_pembeli, _tanggal, _keterangan))
            conn.commit()
            response = jsonify('Barang updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update transaksi.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

    def delete(self, id_transaksi):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute('delete from barang where id_transaksi = %s',id_transaksi)
            conn.commit()
            response = jsonify('Barang deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete barang.')         
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()    
            return(response)       

#API resource routes
api.add_resource(ListPembeli, '/pembeli', endpoint='list-pembeli')
api.add_resource(Pembeli, '/pembeli/<int:id_pembeli>', endpoint='pembeli')
api.add_resource(ListBarang, '/barang', endpoint='list-barang')
api.add_resource(Barang, '/barang/<int:id_barang>', endpoint='barang')
api.add_resource(ListTransaksi, '/transaksi', endpoint='list-transaksi')
api.add_resource(Transaksi, '/transaksi/<int:id_transaksi>', endpoint='transaksi')

if __name__ == "__main__":
    app.run(debug=True)