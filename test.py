import datastore

#To create a specific directory
datastore.create_dir('yes') #to provide a specific directory

#To create a non specific directory
datastore.create_dir('no')

#To Create a Key-value pair
datastore.create('key','value')

#To read the value for the provided key
datastore.read('key')

#To remove the value for the provided key
datastore.remove('key')
