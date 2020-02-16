# Program to print if the string in a list have more than 5 characters
lst = ['hemsunder', 'durga', 'selenium', 'python', 'cmd', 'java']


def output(lst):
    for i in lst:
        if len(i)>5:
            print(i)


output(lst)


# Output:
# hemsunder
# selenium
# python