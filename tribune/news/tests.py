from django.test import TestCase
from .models import Editor,Article,tags

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))


    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

        # Testing Delete Method
    def test_delete_method(self):
        self.james.save_editor()
        self.james.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        self.blog=Article(title = 'Breaking news', post = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',pub_date = '2019-02-02')

    def test_instance(self):
        self.assertTrue(isinstance(self.blog,Article))

    def test_save_method(self):
        self.blog.save_Article()
        articles = Article.objects.all()
        self.assertTrue(len(articles) > 0)
