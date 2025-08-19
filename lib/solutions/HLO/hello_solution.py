
class HelloSolution:
    
    # friend_name = unicode string
    def hello(self, friend_name):
        if isinstance(friend_name, str):
            return('hello '+friend_name)

