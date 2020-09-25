import random
import math
from util import Queue  # These may come in handy

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Calculate max num of friends a user can have
        # cap_friends = math.ceil(num_users * .25)

        # Calculate total connections between users
        total_friendships = num_users * avg_friendships
        # keep track of actual friends added
        added_count = 0
        # Add users

        for i in range(1, num_users+1):
            self.add_user(i)

        # Create friendships

        for i in range(1, num_users+1):
            if added_count < total_friendships:
                # on odd num users, calculate randomly how many friends they should get
                if i%2 != 0:
                    add_friends = random.randint(0, i-1)
                    while add_friends > 0:
                        if added_count >= total_friendships:
                            add_friends = 0
                            continue
                        random_friend = random.randint(1, num_users)
                        if random_friend != i:
                            if random_friend not in self.friendships[i]:
                                self.add_friendship(i, random_friend)
                                add_friends -= 1
                                added_count += 2
                # on even num users, calculate how many friends are needed to keep avg
                    # randomly generate number below i based on needed friend to keep avg
                else:
                    to_add = (avg_friendships * i) - added_count
                    
                    if to_add > i:
                        to_add = i
                    while to_add > 0:
                        if added_count >= total_friendships:
                            to_add = 0
                            continue
                        random_friend = random.randint(1, num_users)
                        if random_friend != i:
                            if random_friend not in self.friendships[i]:
                                self.add_friendship(i, random_friend)
                                to_add -= 1
                                added_count += 2
        
        # while added_count < total_friendships:
        #     for i in range(num_users):
        #         # self.add_user(i+1)
        #         # print(i)
        #     # Create friendships
        #         print(added_count)
        #         if added_count >= total_friendships:
        #             continue
        #         count = 0
        #         for j in range(1, i):
        #             # print(j)
        #             something = round(random.random())
        #             # print(f"User {i}: {count}, {cap_friends}")
        #             j_friend = self.friendships[j]
        #             if something and len(j_friend) < cap_friends:
        #                 self.add_friendship(i+1, j)
        #                 count += 1
        #                 added_count += 1
        print(total_friendships, added_count)
    
        

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
​
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
​
        The key is the friend's ID and the value is the path.
​
        BFT
        
        Shortest path --> breadth first
        Recursion --> depth first
​
        """
        q = Queue()
        visited = {}  # Note that this is a dictionary, not a set

        q.enqueue([user_id])

        while q.size() > 0:
            current_path = q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:
                visited[current_user] = current_path

                friends = self.friendships[current_user]

                for friend in friends:
                    path_copy = list(current_path)
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited


from timeit import default_timer as timer
if __name__ == '__main__':
    sg = SocialGraph()
    start = timer()
    sg.populate_graph(100, 5)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    elapsed_time = timer() - start # in seconds
    print("Elapsed Time: ", elapsed_time)
    print("\n")
