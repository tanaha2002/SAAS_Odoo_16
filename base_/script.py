import xmlrpc.client
import sys
url = 'http://localhost:8069'
db = sys.argv[1]
user = 'admin'
password = 'admin123@'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, user, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_name = 'activate.ssl'
function_name = 'activate_ssl'
try:
    #execute function and give parameters db_name
    result = models.execute_kw(db, uid, password, model_name, function_name, [[]])
    print(result)
except Exception as e:
    print(f'Error executing the function: {str(e)}')
