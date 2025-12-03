from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, HelpPanel
from wagtail.search import index

from blog.blocks import BaseStreamBlock


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    subpage_types = ['blog.BlogPage']


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField(BaseStreamBlock())

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        HelpPanel(
            content=(
                'Please ensure that you do not skip heading levels. '
            'For example, the next heading after an H2 '
            'should only be either an H3 or another H2. '
            '<a href="https://www.a11yproject.com/posts/'
            'how-to-accessible-heading-structure/" target="_blank">'
            'Learn more about heading structure</a>'
            )
        ),
        FieldPanel('body'),
    ]

    parent_page_types = ['blog.BlogIndexPage']