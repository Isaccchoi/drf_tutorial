from django.conf import settings
from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='snippets',
                              on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    highlighted = models.TextField(blank=True)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        # self.language에 ㅐ당하는 이름의 lexer를 지정
        lexer = get_lexer_by_name(self.language)
        # self.linenos가 True일 경우 'table', 아니면 False를 linenos에 해당
        linenos = self.linenos and 'table' or False
        # self.title이 존재할 경우 {'title': self.title}dict를 아니면  {} dict를 options에 할당
        options = self.title and {'title': self.title} or {}
        # pygments의 HtmlFormatter 인스턴스를 생성
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        # self.higlighted필드에 highlight함수에 self.code를 지정한 결과값을 대입
        self.highlighted = highlight(self.code, lexer, formatter)
        # 이후 진행되던 save 호출
        super(Snippet, self).save(*args, **kwargs)
