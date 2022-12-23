#!/usr/bin/env python3

import sys
import os
import os.path
from os import path
import time
import shutil
import subprocess

cdb_home_dir = os.getenv('HOME')
template_base_dir = cdb_home_dir + "/" + "cdb-support/customization/templates"
temp_base_dir = "/tmp/" + str(time.time()) # create subdirectory with epoch time for uniqueness

def fatal_error(msg):
    print("##### FATAL ERROR #####")
    print(msg)
    sys.exit(1)

def validate_environment_variable(name, value):
    if (value is None or value == ""):
        fatal_error("no value specified for $%s variable" % name)

def run_subprocess(commandArray):
    result = subprocess.run(commandArray, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    print("running: %s" % str(commandArray))
    print("stdout: ", result.stdout)
    print("stderr: ", result.stderr)

def pre_customize_processing():
    
    print()
    print("===== pre-customization processing =====")
    print()

    print("setting permissive selinux permissions to make nginx happy...")
    run_subprocess([cdb_home_dir + "/cdb-support/bin/selinux-permissive"])
    
def customize_nginx():

    # get environment variables for template replacement
    subdomain = os.getenv('REPL_SUBDOMAIN')
    tls_cert_path = os.getenv('REPL_TLS_CERT_PATH')
    tls_key_path = os.getenv('REPL_TLS_KEY_PATH')
    nginx_config_path = os.getenv('REPL_NGINX_CONFIG_PATH')
    nginx_config_filename = os.getenv('REPL_NGINX_CONFIG_FILENAME')
    nginx_repo_path = os.getenv('REPL_NGINX_REPO_PATH')

    # validate environment variables
    validate_environment_variable("REPL_SUBDOMAIN", subdomain)
    validate_environment_variable("REPL_TLS_CERT_PATH", tls_cert_path)
    validate_environment_variable("REPL_TLS_KEY_PATH", tls_key_path)
    validate_environment_variable("REPL_NGINX_CONFIG_PATH", nginx_config_path)
    validate_environment_variable("REPL_NGINX_CONFIG_FILENAME", nginx_config_filename)
    validate_environment_variable("REPL_NGINX_REPO_PATH", nginx_repo_path)

    # check that directories exist
    if not path.exists(tls_cert_path):
        fatal_error("invalid directory %s specified by $REPL_TLS_CERT_PATH" % tls_cert_path)
    if not path.exists(tls_key_path):
        fatal_error("invalid directory %s specified by $REPL_TLS_KEY_PATH" % tls_key_path)
    if not path.exists(nginx_repo_path):
        fatal_error("invalid directory %s specified by $REPL_NGINX_REPO_PATH" % nginx_repo_path)

    # determine directory and file paths
    nginx_dir_name = "nginx"
    nginx_template_dir = template_base_dir + "/" + nginx_dir_name
    nginx_temp_dir = temp_base_dir + "/" + nginx_dir_name
    nginx_template_file_path = nginx_template_dir + "/" + nginx_config_filename
    nginx_temp_file = nginx_temp_dir + "/" + nginx_config_filename
    nginx_config_file_path = nginx_config_path + "/" + nginx_config_filename
    nginx_repo_file_path = nginx_repo_path + "/" + nginx_config_filename
    
    print()
    print("===== customizing nginx ====")
    print()
    print("subdomain: %s" % subdomain)
    print("tls_cert_path: %s" % tls_cert_path)
    print("tls_key_path: %s" % tls_key_path)
    print("nginx template dir: %s" % nginx_template_dir)
    print("nginx template file path: %s" % nginx_template_file_path)
    print("nginx temp dir: %s" % nginx_temp_dir)
    print("nginx temp file: %s" % nginx_temp_file)
    print("nginx config dir: %s" % nginx_config_path)
    print("nginx config filename: %s" % nginx_config_filename)
    print("nginx config file path: %s" % nginx_config_file_path)
    print("nginx repo file path: %s" % nginx_repo_file_path)
    
    print("nginx repo path: %s" % nginx_repo_path)

    # check existence of template file
    if not path.exists(nginx_template_file_path):
        fatal_error("nginx template file %s does not exist" % nginx_template_file_path)

    # check existence of config directory
    if not path.exists(nginx_config_path):
        fatal_error("nginx config directory %s not found" % nginx_config_path)

    # create tmp directory
    os.makedirs(nginx_temp_dir, 0o700, False)

    # copy template file to tmp directory
    shutil.copy2(nginx_template_file_path, nginx_temp_dir)

    # validate and read temp file and replace specified strings from template
    if not path.exists(nginx_temp_file):
        fatal_error("error creating nginx temp file: %s" % nginx_temp_file)
    fin = open(nginx_temp_file, "rt") # open temp file for read
    data = fin.read() # read file data
    data = data.replace("##REPL_SUBDOMAIN##", subdomain) # replace subdomain variable
    data = data.replace("##REPL_TLS_CERT_PATH##", tls_cert_path) # replace tls cert path
    data = data.replace("##REPL_TLS_KEY_PATH##", tls_key_path) # replace tls key path
    fin.close()
    fin = open(nginx_temp_file, "wt")
    fin.write(data)
    fin.close()

    # copy temp file to config directory
    shutil.copy2(nginx_temp_file, nginx_config_path)
    if not path.exists(nginx_config_file_path):
        fatal_error("error copying to nginx config file %s" % nginx_config_file_path)

    # copy new config file to version controlled directory since can't use sym links under github
    shutil.copy2(nginx_temp_file, nginx_repo_path)
    if not path.exists(nginx_repo_file_path):
        fatal_error("error copying to nginx repo file %s" % nginx_repo_file_path)

    print()
    print("installed nginx config file: %s" % nginx_config_file_path)
    print("installed nginx repo file: %s" % nginx_repo_file_path)

def post_customize_processing():

    print()
    print("===== post-customization processing =====")
    print()

    print("restarting nginx...")
    run_subprocess(["/bin/sudo", "systemctl", "restart", "nginx"])
    
def main():

    print()
    print("===== ecosystem-customize.py =====")
    print()
    print("cdb home dir: %s" % cdb_home_dir)
    print("template base dir: %s" % template_base_dir)
    print("temp base dir: %s" % temp_base_dir)

    pre_customize_processing()    
    customize_nginx()
    post_customize_processing()
    
if __name__ == "__main__":
    main()

