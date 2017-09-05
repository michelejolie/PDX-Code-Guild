# def make_html(tag, contents):
#     return '<{0}> {1} </{0}>'.format(tag, contents)
#
# def print_msg(msg):
#     message = msg
#
#     def printer():
#         print(message)
#
#     return printer
#
#
# world = print_msg('Hello, World!')
#
# chris = print_msg('Hello, Chris!')
#
# world()
# chris()


def make_html_p(function, *args, **kwargs):
    def inner(args):
        return '<p> {} </p>'.format(function(args))
    return inner


@make_html_p
def print_body(body):
    return body


@make_html_p
def print_other(stuff):
    return stuff

print(print_body('this is a message'))
print(print_other('this is another message'))
# def make_multiplier_of(n):
#     def multiplier(x):
#         return x * n
#
#     return multiplier
#
#
# times3 = make_multiplier_of(3)
#
# times5 = make_multiplier_of(5)
#
# print(times3(9))
