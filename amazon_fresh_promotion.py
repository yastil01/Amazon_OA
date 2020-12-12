def is_amazon_fresh_winner(code_list, shopping_cart):
    i = j = 0
    code_index = 0
    while code_index < len(code_list) and i < len(shopping_cart):
        j = 0
        while j < len(code_list[code_index]) and i < len(shopping_cart):
            if code_list[code_index][j] == shopping_cart[i] or code_list[code_index][j] == 'anything':
                j += 1
            else:
                j = 0
                while code_list[code_index][j] == 'anything':
                    j += 1
            i += 1

        code_index += 1
    if code_index == len(code_list) and j == len(code_list[-1]):
        return 1
    return 0


code_list = [['anything', 'anything', 'apple'], ['banana', 'anything', 'banana']]
shopping_cart = ['orange', 'grapes', 'orange', 'apple', 'orange', 'orange', 'banana', 'apple', 'banana', 'banana']
assert is_amazon_fresh_winner(code_list, shopping_cart) == 1

code_list = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shopping_cart = ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']
assert is_amazon_fresh_winner(code_list, shopping_cart) == 1

code_list = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shopping_cart = ['banana', 'orange', 'banana', 'apple', 'apple']
assert is_amazon_fresh_winner(code_list, shopping_cart) == 0

code_list = [['apple', 'apple'], ['banana', 'anything', 'banana']]
shopping_cart = ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']
assert is_amazon_fresh_winner(code_list, shopping_cart) == 0

code_list = [['apple', 'apple'], ['apple', 'apple', 'banana']]
shopping_cart = ['apple', 'apple', 'apple', 'banana']
assert is_amazon_fresh_winner(code_list, shopping_cart) == 0
