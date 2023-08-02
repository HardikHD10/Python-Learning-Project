class BlogPost:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated(function):
    def wrapper(*args):
        if args[0].is_logged_in:
            function(args[0])

    return wrapper


@is_authenticated
def create_blog_post(user):
    print(f"This is {user.name}'s blog post!")


blogpost = BlogPost("Hardik")
blogpost.is_logged_in = True
create_blog_post(blogpost)
