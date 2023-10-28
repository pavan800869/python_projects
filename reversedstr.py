class ReversedStr(str):
    def __new__(*args, **kwargs):
        self = str.__new__(*args, **kwargs)
        self = self[::-1]
        return self
    
# This class is used to reverse the entered string.
# We don't get self in new method because new is a special method and it is a class method. 