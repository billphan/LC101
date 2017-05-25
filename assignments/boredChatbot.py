# Chapter 13 Weekly Graded Assignment

class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """
    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

# TODO define a class called BoredChatbot
class boredChatbot(Chatbot):
    # define a function taking self, and astring as paremter
    def boredNow(self, astring):
        # if length of input astring larger than 20 char...
        if len(astring) > 20:
            # return bored statement
            print("zzz... Oh excuse me, I dozed off reading your essay.")
        # elif len(astring) > 10:
        #     print("Very interesting...")
        else:
            # else return normal response
            print(Chatbot.response(self, astring))

# test results
wally = boredChatbot("Wally")
astring = input(wally.greeting())
boredChatbot.boredNow(wally, astring)
