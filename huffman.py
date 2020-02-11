class Node:

    # def __init__(self, char, frequence, left = None, right = None, leaf = False):
    # Charactersitics of the tree
    def __init__(self, char, frequence, left = None, right = None, leaf = False):
            self.leftChild = left
            self.rightChild = right
            self.char = char
            self.freq = frequence
            self.leaf = leaf

    # def __lt__(self, other):
    # Used for comparing the frequencies in Huffman Tree
    def __lt__(self, other):
        return (self.freq < other.freq)

class Huffman_Code:

    # def frequencies(self, message):
    # Creates a dictionary of frequencies which is made
    # by the counting of each character passed in by the user
    # It then is added to the dictionary and returned back to be used
    # in creating the tree
    def frequencies(self, message):
        frequences = {}
        for char in message:
            if not char in frequences:
                frequences[char] = 0
            frequences[char] += 1
        return frequences

    # def minimal_node(self, tree):
    # Finds the minimal nodes (at the base) which allows
    # for the tree to be created, by starting at the base, and working
    # the way up.
    def minimal_node(self, tree):
        if len(tree) == 1:
            return 0
        if len(tree) == 0:
            return -1
        min_node = 0
        for i,v in enumerate(tree):
            if v<tree[min_node] :
                min_node = i
        return min_node

    # def Tree(self, frequences):
    # This method creates the tree by appedning the frequencies
    # to the tree then addidng them, by popping off and returning
    # the newer nodes added together, until all that is left 
    # is one final tree
    def Tree(self, frequences):
        tree = list()

        for char in frequences :
            tree.append(Node(char, frequences[char], leaf=True))
            
        while(len(tree)>1):
            min_node = self.minimal_node(tree)
            first_Node = tree.pop(min_node)
            min_node_2 = self.minimal_node(tree)
            second_Node = tree.pop(min_node_2)
            newest_Node = Node(first_Node.char + second_Node.char, 
            first_Node.freq + second_Node.freq,
            first_Node, second_Node)
            tree.append(newest_Node)

        return tree[0]

    # def coding(self, tree, frequences):
    # This passes in the tree, and the frequencies which
    # then gives the nodes a 1 or 0 based upon if the characters are left
    # or right children.
    def coding(self, tree, frequences):
        code = {}
        for key in frequences:
            current_node = tree
            sequence = ''
            while not (current_node.leaf):
                if key in current_node.leftChild.char :
                    sequence = sequence + '0'
                    current_node = current_node.leftChild
                elif key in current_node.rightChild.char :
                    sequence = sequence + '1'
                    current_node = current_node.rightChild
                else:
                    raise Exception
            code[key] = sequence
        return code

    # def encoding(self, codex, text):
    # This makes the reduced huffman code of the tree, based off of the
    # text and the coding of the tree
    def encoding(self, codex, text):
        binary_coding = ''
        for char in text :
            binary_coding += codex[char]
        return binary_coding

    # def decoding(self, codex, binary_coding):
    # This passes in the binary string by user and
    # the coding of the tree, which then goes through and finds
    # the list of 1's and 0's which the user wanted to find
    def decoding(self, codex, binary_coding):
        text = ''
        binary_code = binary_coding
        while len (binary_code) > 0:
            index = 1
            next_character = False
            while not next_character:
                for key in codex:
                    if codex[key] == binary_code[:index]:
                        text += key
                        next_character = True
                    else:
                        raise Exception
                index += 1
            binary_code = binary_code[index-1:]
        return text

    # def __init__(self, text):
    # Initiating the user text
    def __init__(self, text):
        self.text = text

# if __name__ =='__main__' :
# Asks for user inputted text, goes through the coding, frequency creation,
# and tree creation of the Huffman code. Then encodes the text and prints
# it out for the user to see. It then asks for 1's or 0's for the user to
# input for decoding the tree, and then it prints out the numbers accordingly.
if __name__ =='__main__' :
    user_input = input("Please input your string: ")
    user_input = user_input.lower()
    huffmanCode = Huffman_Code(user_input)

    frequency = huffmanCode.frequencies(user_input)
    tree = huffmanCode.Tree(frequency)
    codex = huffmanCode.coding(tree, frequency)
    encoded_text = huffmanCode.encoding(codex, user_input)
    print("Your encoded text: ", encoded_text)

    user_decoded_text = input("Please input a binary string of '1''s and/or '0''s: ")
    decoding_user_text = huffmanCode.decoding(codex, user_decoded_text)
    print("Your decoded text: ", decoding_user_text)