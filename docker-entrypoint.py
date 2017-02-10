#!/usr/bin/python
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from sys import argv
import os

def write_config_file(input_path, output_path):
    with open(input_path, 'r') as input_file:
        cfg = load(input_file.read())
    if cfg['haproxy'] == None:
        cfg['haproxy'] = {}
    cfg['haproxy']['config_file_path'] = '/etc/haproxy/haproxy.cfg'
    cfg['haproxy']['reload_command'] = 'supervisorctl restart haproxy'
    with open(output_path, 'w+') as output_file:
        output_file.write(dump(cfg))

def execempty(f):
    os.execl(f, f)

if argv[1] == 'synapse':
    write_config_file(argv[2], '/etc/smartstack/synapse/config.yml')
    execempty('/usr/bin/supervisord')
else:
    os.execv(argv[1], argv[1:])
