''' RemoveTag '''
import re

def removetag(text):
    ''' remove html '''
    head = re.compile(r'<[^>]+>')
    tag = ''.join(head.sub(' ', text))
    return tag.split()
print(removetag(text=input()))
