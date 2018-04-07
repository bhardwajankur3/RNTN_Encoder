class Node():

    def __init__(self, word=None):
        self.word = word
        self.left = None
        self.right = None
        self.word_vector = None

    def is_leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def word_yield(self):
        if self.left is None and self.right is None:
            return self.word

        ans=''
        if self.left:
            ans=ans+self.left.word_yield()
        if self.right:
            ans=ans+' '+self.right.word_yield()
        return ans

    def clone(self):
        ans=Node()
        ans.word=self.word
        ans.word_vector=self.word_vector
        if self.left:
            ans.left=self.left.clone()
        if self.right:
            ans.right=self.right.clone()
        return ans