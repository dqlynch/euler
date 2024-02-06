all:

.PHONY: all

Makefile: ;

%: kitty $@
	time cat $@ | ./kitty

kitty: kitty_2.cpp
	g++ -std=c++2a -Wpedantic -Wall -O2 kitty_2.cpp -o kitty
