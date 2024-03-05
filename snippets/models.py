from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


from django.utils.timezone import now

LANGUAGE_CHOICES = [
    ("python", "Python"),
    ("react", "React"),
    ("js", "JavaScript"),
    ("css", "CSS"),
    ("html", "HTML"),
    ("git", "Git"),
]

TAG_CHOICES = [
        ('Python', (
            ('date', 'Date'),
            ('dictionary', 'Dictionary'),
            ('function', 'Function'),
            ('index', 'Python Snippets'),
            ('list', 'List'),
            ('math', 'Math'),
            ('string', 'String'),
        )
         ),
        ('React', (
            ('components', 'Components'),
            ('hooks', 'Hooks'),
            ('index', 'React Snippets'),
            ('rendering', 'Rendering'),
            ('testing', 'Testing'),
            ('cheatsheets', 'Cheatsheets'),
            ('main_listing', 'Main Listing'),
            ('tips', 'Tips'),
            ('webdev', 'Web Development'),
        )
         ),
        ('JavaScript', (
            ('algorithm', 'Algorithms'),
            ('array_initialization', 'Array Initialization'),
            ('array_methods', 'Array Methods'),
            ('array', 'Array Snippets'),
            ('arrow_functions', 'Arrow Functions'),
            ('browser', 'Browser Snippets'),
            ('colors', 'Colors'),
            ('comparison', 'Comparison'),
            ('css_manipulation', 'CSS Manipulation'),
            ('data_structures', 'Data Structures'),
            ('date', 'Dates'),
            ('dom_manipulation', 'DOM Manipulation'),
            ('event_handling', 'Event Handling'),
            ('function', 'Function Snippets'),
            ('functional_programming', 'Functional Programming'),
            ('generators', 'Generator Functions'),
            ('geometry', 'Geometric Operations'),
            ('http_requests', 'HTTP Requests'),
            ('index', 'JS Snippets'),
            ('interviews', 'Interview Questions'),
            ('math', 'Math Snippets'),
            ('node', 'Node.js Snippets'),
            ('object_key_transformations', 'JS Object Key Transformations'),
            ('object', 'Object Snippets'),
            ('performance', 'Performance Optimization'),
            ('promises', 'Promises'),
            ('proxy', 'Proxy'),
            ('random_value_generators', 'Random Value Generators'),
            ('scroll', 'Browser Scrolling'),
            ('string', 'String'),
            ('type', 'Types'),
            ('unit_conversions', 'Unit Conversions'),
            ('url', 'URLs'),
            ('web_storage_essentials', 'Web Storage Essentials'),
        )
         ),
        ('CSS', (
            ('animation', 'Animations'),
            ('background_patterns', 'Background Patterns'),
            ('button_transitions', 'Button Transitions'),
            ('centering', 'Centering'),
            ('hover_effects', 'Hover Effects'),
            ('index', 'CSS Snippets'),
            ('interactivity', 'Interactivity Snippets'),
            ('layout', 'Layouts'),
            ('visual', 'Visual Snippets'),
        )
         ),
        ('HTML', (
            ('head_basics', 'Head Basics'),
            ('index', 'HTML Snippets'),
        )
         ),
        ('Git', (
            ('branch', 'Branch Snippets'),
            ('commit', 'Commit Snippets'),
            ('configuration', 'Configuration Snippets'),
            ('index', 'Git Snippets'),
            ('repository', 'Git Repository Snippets'),
        )
         ),
    ]


class Code(models.Model):
    title = models.CharField(max_length=100)
    text = CKEditor5Field('Text', config_name='extends')
    code = models.TextField()
    language = models.CharField(
        max_length=40,
        choices=LANGUAGE_CHOICES,
    )
    short_definition = models.CharField(max_length=255)
    tags = models.CharField(max_length=40, default='Snippet')
    snippet_image = models.URLField(default='https://i.pinimg.com/564x/bb/42/d1/bb42d137e3ad0bbcc44bc37e1c8ad00e.jpg')
    date = models.DateTimeField(default=now)

    class Meta:
        db_table = 'Code'
        ordering = ['-date']

    def __str__(self):
        return f"{self.language}, {self.title}"






