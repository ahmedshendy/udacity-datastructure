class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users[user] = True

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
p_user = "sub_child_userdd"
parent.add_user(p_user)
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_users = group.get_users()
    if group_users.get(user, False):
        return True
    else:
        inner_groups_list = group.get_groups()
        for inner_group in inner_groups_list:
            return is_user_in_group(user, inner_group)
    
    return False

print(is_user_in_group("sub_child_user", parent))
# True

all_users = Group("All Users")
it_users = Group("IT Users")
all_users.add_group(it_users)
managers_users = Group("Managers Users")
all_users.add_group(managers_users)
all_users.add_user('general')
it_users.add_user('support1')
managers_users.add_user('manager1')


print(is_user_in_group('test', all_users))
# False
print(is_user_in_group('general', all_users))
# True
print(is_user_in_group('general', it_users))
# False
print(is_user_in_group('support1', all_users))
# True
print(is_user_in_group('support1', it_users))
# True
print(is_user_in_group('manager1', it_users))
# False
print(is_user_in_group('general', it_users))
# False