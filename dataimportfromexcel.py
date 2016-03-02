import xmlrpclib
import csv
username = "admin"
pwd = "odoo"
dbname = "OMS"
sock_common = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/common")
uid = sock_common.login(dbname, username, pwd)
sock = xmlrpclib.ServerProxy("http://localhost:8069/xmlrpc/object")
reader = csv.reader(open('hr.employee.csv','rb'))
for row in reader:
	hr_employee_data = {
	'contract_ids.name' : row[1],
	'contract_ids.type_id.id' : row[2],
	'name' : row[6],
	'default_code' : row[0],
	'active' : True,
	}
	template_id = sock.execute(dbname, uid,pwd, 'hr.employee','create',hr_employee_data)
