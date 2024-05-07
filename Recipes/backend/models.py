from backend.database.exts import db

class Recipe(db.Model):
    """
        class Recipe:
        id: int pk
        title: str 
        description: str
    """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f"<Recipe {self.title} >"

    def save(self):
        """
        The save function is used to save the changes made to a model instance.
        It takes in no arguments and returns nothing.

        Params:
        self: Refer to the current instance of the class

        Return:
        The object that was just saved
        """
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """
        The delete function is used to delete a specific row in the database. It takes no parameters and returns nothing.
        """
        db.session.delete(self)
        db.session.commit()

    def update(self, title, description):
        """
        The update function updates the title and description of a given blog post.
        It takes two parameters, title and description.

        Params:
        title: Update the title of the post
        description: Update the description of the blog post

        Return:
        A dictionary with the updated values of title and description
        """
        self.title = title
        self.description = description

        db.session.commit()

class User(db.Model):
    """
    class User:
        id: integer
        username: string
        email: string
        password: string
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        """
        returns string rep of object

        """
        return f"<User {self.username}>"

    def save(self):
        """
        The save function is used to save the changes made to a model instance.
        """
        db.session.add(self)
        db.session.commit()
