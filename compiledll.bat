@echo off

clang++ -c -o random.o random.cxx
clang++ -shared -v -o random.dll random.o