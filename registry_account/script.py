import xmlrpc.client
import sys
import config as cf
url = cf.url
db  = sys.argv[1]
user = cf.base_login
password = cf.base_passwd

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, user, password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
model_name = 'activate.ssl'
function_name = 'activate_ssl'
try:
    #execute function and give parameters db_name
    result = models.execute_kw(db, uid, password, model_name, function_name, [[]])
    print(result)
    #return exec of this file to check in parent file
    sys.exit(0)
except Exception as e:
    print(f'Error executing the function: {str(e)}')

