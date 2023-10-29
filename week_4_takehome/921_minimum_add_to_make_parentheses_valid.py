import matplotlib.pyplot as plt

def visualize_min_add_to_make_valid(s):
    balance = ans = 0
    balances = [0]
    
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == -1:
            ans += 1
            balance += 1
        balances.append(balance)

    plt.plot(balances, marker='o')
    plt.axhline(0, color='grey', linewidth=0.7)
    plt.title('Parentheses Balance Visualization')
    plt.xlabel('Character Position')
    plt.ylabel('Balance')
    plt.show()

    print("Minimum Additions Required:", ans + balance)

s1 = "())"
s2 = "((("

visualize_min_add_to_make_valid(s1)
visualize_min_add_to_make_valid(s2)


def minAddToMakeValid(s):
    balance = ans = 0
    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == -1:
            ans += 1
            balance += 1
    return ans + balance

