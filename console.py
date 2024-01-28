#!/usr/bin/python3
# bash script implementing a shell-like prototypig tool

import cmd
import readline

class HBNBCommand(cmd.Cmd):
    """ my prototyping tool for the Airbnb clone project """
    prompt = '(hbnb)'

    def do_quit(self, line):
        """ quit the proto tool"""
        print('see you!')
        return True
    def help_quit(self):
        """describe what quit does"""
        print('Ibra')

    def do_EOF(self, line):
        """exit gracefully """
        print()
        return True
    def message(self, mess):
        print(mess)

    def do_greet(self, perso):
        """ greet perso"""
        if perso:
            print('Hello,')
        else:
            print('Hi')

        print(f'I Love you so much {perso}')
if __name__ == '__main__':
    HBNBCommand().cmdloop(intro='Welcome!')
