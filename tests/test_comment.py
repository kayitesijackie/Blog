from app.models import Comment,User,Blog
from app import db
import unittest

class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_Blog = Blog(id=1,pitch_title='Test',blog_content='This is a test blog',category="success",user = self.user_James)
        self.new_comment = Comment(id=1,comment='Test comment',user=self.user_James,blog=self.new_blog)

    def tearDown(self):
        Blog.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.comment,'Test comment')
        self.assertEquals(self.new_comment.user,self.user_James)
        self.assertEquals(self.new_comment.blog,self.new_blog)
