#!/usr/bin/python3
""" my console """

import cmd
import readline


class HBNBCommand(cmd.Cmd):
    """ my prototyping tool for the Airbnb clone project """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ quit the proto tool"""
        return True
    def help_quit(self):
        """describe what quit does"""
        print('some info')

    def do_EOF(self, line):
        """exit gracefully """
        print()
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop(intro='Welcome!')
