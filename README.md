# Freshworks_datastore
Datastore.py Libarary File contains four methods:
*datastore.create_dir() - which creates user specified directory if provided one or creates one on it's own.
*datastore.create()- which creates a Key-value pair given by the user.
*datastore.read()- which prints the value according to the key provided by the user.
*datastore.remove()- which removes the value according to the key provided by the user.
A Time to Live property is used for every key value pair that has been created. The Provided time for a key is 24hours, if exceeded the key cannot the read or removed from the file.
The data.json file has been created with a storage limit of 1GB or 1000mb.
