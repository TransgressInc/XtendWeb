#!/usr/bin/env python


import cgitb
import subprocess
import cgi
import psutil
import os
import yaml

__author__ = "Anoop P Alias"
__copyright__ = "Copyright Anoop P Alias"
__license__ = "GPL"
__email__ = "anoopalias01@gmail.com"


installation_path = "/opt/nDeploy"  # Absolute Installation Path
xtendweb_installation_path = "/opt/nDeploy"  # Absolute Installation Path
backend_config_file = installation_path+"/conf/backends.yaml"


def branding_print_logo_name():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_logo = yaml_parsed_brand.get("brand_logo", "xtendweb.png")
    else:
        brand_logo = "xtendweb.png"
    return brand_logo


def branding_print_banner():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_name = yaml_parsed_brand.get("brand", "XtendWeb")
    else:
        brand_name = "XtendWeb"
    return brand_name


def branding_print_footer():
    "Branding support"
    if os.path.isfile(installation_path+"/conf/branding.yaml"):
        with open(installation_path+"/conf/branding.yaml", 'r') as brand_data_file:
            yaml_parsed_brand = yaml.safe_load(brand_data_file)
        brand_footer = yaml_parsed_brand.get("brand_footer", '<a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">A U T O M 8 N</a>')
    else:
        brand_footer = '<a target="_blank" href="https://autom8n.com/xtendweb/UserDocs.html">A U T O M 8 N</a>'
    return brand_footer


cgitb.enable()
form = cgi.FieldStorage()

print('Content-Type: text/html')
print('')
print('<html>')
print('<head>')

print('<title>')
print(branding_print_banner())
print('</title>')

print(('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">'))
print(('<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" crossorigin="anonymous"></script>'))
print(('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>'))
print(('<script src="js.js"></script>'))
print(('<link rel="stylesheet" href="styles.css">'))
print('</head>')
print('<body>')
print('<div id="main-container" class="container text-center">')  # marker1
print('<div class="row">')  # marker2
print('<div class="col-md-6 col-md-offset-3">')  # marker3

print('<div class="logo">')
print('<a href="xtendweb.cgi"><img border="0" src="')
print(branding_print_logo_name())
print('" width="48" height="48"></a>')
print('<h4>')
print(branding_print_banner())
print('</h4>')
print('</div>')

print('<ol class="breadcrumb">')
print('<li><a href="xtendweb.cgi"><span class="glyphicon glyphicon-repeat"></span></a></li>')
print('<li class="active">Server Config</li>')
print('</ol>')

if form.getvalue('mode') and form.getvalue('unit') and form.getvalue('cpu') and form.getvalue('memory') and form.getvalue('blockio'):
    if form.getvalue('mode') == 'service':
        myservice = form.getvalue('unit')+".service"
        print('<div class="panel panel-default">')
        print(('<div class="panel-heading"><h3 class="panel-title">Save Resource limit:'+myservice+'</h3></div>'))
        print('<div class="panel-body">')  # marker6
        if form.getvalue('cpu') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=256', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=256"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('cpu') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=512', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=512"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('cpu') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=768', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=768"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('cpu') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=1024', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=1024"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('blockio') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('blockio') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('blockio') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('blockio') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        mymem = psutil.virtual_memory().total
        mem_quarter = float(mymem) * 0.25
        mem_threequarter = float(mymem) * 0.75
        mem_half = float(mymem) / 2.0
        if form.getvalue('memory') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('memory') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('memory') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('memory') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(mymem), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mymem))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl daemon-reload', shell=True)
        if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
            with open(os.devnull, 'w') as FNULL:
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl daemon-reload"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
    elif form.getvalue('mode') == 'user':
        print('<div class="panel panel-default">')
        print(('<div class="panel-heading"><h3 class="panel-title">Save Resource limit:'+form.getvalue('unit')+'</h3></div>'))
        print('<div class="panel-body">')  # marker6
        with open(backend_config_file, 'r') as backend_data_yaml:
            backend_data_yaml_parsed = yaml.safe_load(backend_data_yaml)
        php_backends_dict = backend_data_yaml_parsed["PHP"]
        myservice = 'ndeploy_hhvm@'+form.getvalue('unit')+".service"
        if form.getvalue('cpu') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=256', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=256"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('cpu') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=512', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=512"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('cpu') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=768', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=768"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('cpu') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=1024', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=1024"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('blockio') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('blockio') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('blockio') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('blockio') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        mymem = psutil.virtual_memory().total
        mem_quarter = float(mymem) * 0.25
        mem_threequarter = float(mymem) * 0.75
        mem_half = float(mymem) / 2.0
        if form.getvalue('memory') == '25':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        if form.getvalue('memory') == '50':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('memory') == '75':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter)), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        elif form.getvalue('memory') == '100':
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(mymem), shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mymem))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes', shell=True)
        subprocess.call('/usr/bin/systemctl daemon-reload', shell=True)
        if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
            with open(os.devnull, 'w') as FNULL:
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl daemon-reload"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
        for backend_name in list(php_backends_dict.keys()):
            myservice = backend_name+'@'+form.getvalue('unit')+".service"
            if form.getvalue('cpu') == '25':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=256', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=256"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            if form.getvalue('cpu') == '50':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=512', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=512"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('cpu') == '75':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=768', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=768"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('cpu') == '100':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUShares=1024', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUShares=1024"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            if form.getvalue('blockio') == '25':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=250"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            if form.getvalue('blockio') == '50':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=500"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('blockio') == '75':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=750"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('blockio') == '100':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000', shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOWeight=1000"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            mymem = psutil.virtual_memory().total
            mem_quarter = float(mymem) * 0.25
            mem_threequarter = float(mymem) * 0.75
            mem_half = float(mymem) / 2.0
            if form.getvalue('memory') == '25':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter)), shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_quarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            if form.getvalue('memory') == '50':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half)), shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_half))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('memory') == '75':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter)), shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mem_threequarter))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            elif form.getvalue('memory') == '100':
                subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(mymem), shell=True)
                if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                    with open(os.devnull, 'w') as FNULL:
                        subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryLimit='+str(int(mymem))+'"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes', shell=True)
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes', shell=True)
            subprocess.call('/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes', shell=True)
            subprocess.call('/usr/bin/systemctl daemon-reload', shell=True)
            if os.path.isfile('/opt/nDeploy/conf/ndeploy_cluster.yaml'):
                with open(os.devnull, 'w') as FNULL:
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' CPUAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' BlockIOAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl set-property '+myservice+' MemoryAccounting=yes"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
                    subprocess.Popen('ansible -i /opt/nDeploy/conf/nDeploy-cluster/hosts ndeployslaves -a "/usr/bin/systemctl daemon-reload"', stdout=FNULL, stderr=subprocess.STDOUT, shell=True)
    print('<div class="icon-box">')
    print('<span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span> Resource Settings updated')
    print('</div>')

    print('</div>')  # markera2
    print('</div>')  # markera1
else:
    print('<div class="alert alert-info"><span class="glyphicon glyphicon-alert" aria-hidden="true"></span> Forbidden </div>')

print('<div class="panel-footer"><small>')
print(branding_print_footer())
print('</small></div>')

print('</div>')
print('</div>')
print('</div>')
print('</body>')
print('</html>')
