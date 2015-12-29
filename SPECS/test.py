from teapot import builder
import os

name = 'test'
os.chdir(builder.build_root(name))
f = open('hello.txt', mode='w')
f.write('Hello world')
f = open('hello2.txt', mode='w')
f.write('Hello world')
f = open('hello3.txt', mode='w')
f.write('Hello world')
os.mkdir('asdf')
os.chdir('asdf')
f = open('hello.txt', mode='w')
f.write('Hello world')
f = open('hello2.txt', mode='w')
f.write('Hello world')
f = open('hello3.txt', mode='w')
f.write('Hello world')
f.close()