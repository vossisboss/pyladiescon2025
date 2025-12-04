# Step Five: Helping Editors Help Themselves

One of the best ways you can support users is to give them prompt and guidance as they are using your software. Here are some examples of how you can use help text and panels to promote better accessibility practices.


## `help_text`

In Wagtail and Django, help text is a way for developers to provide hints about a field to a user as they are editing it. You can add a `help_text` attribute to most fields to give your user extra instructions.

### Help text for prompting contextual alt text

Help text can provide helpful reminders about alt text fields. While having some alt text, even imperfect alt text, is better than nothing, it's even better to make sure the alt text of the image matches the context of the content you are including the image in. So in our `blocks.py` file, let's update the `image` field to include some `help_text`.

```python
class BaseStreamBlock(StreamBlock):
    heading = HeadingBlock()
    paragraph = RichTextBlock()
    image = ImageBlock(help_text="Change the alt text to match the context of your blog")
    embed = EmbedBlock(max_width=800, max_height=400)
```
After you save your changes and refresh the page, you should see that `help_text` included as a part of the `image` field. It's best to make `help_text`as brief and direct as possible, but you can also include links in your `help_text` with the `mark_safe` method. You can find a good example of that in the prior version of this tutorial in [Step Eight](https://github.com/vossisboss/pyconwagtail2024/tree/step-8).


## `HelpPanel`

Sometimes you might find yourself in a situation where it'd be a better user experience to give guidance at a page level rather than on individual fields. For example, let's say you wanted to include a more general reminder about heading hierarchary on your blog pages.

Wagtail has a `HelpPanel` that is perfect for this kind of situation. Rather than a typical editor panel that provides some sort of form widget for entering content, `HelpPanel` is a way to provide read-only help content to users.

Here's an example of how to include a `HelpPanel` in one of the blog models. Update your `models.py` file in the `blog` application to match this code:

```python
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
```

Help text and help panels are gentler approaches to encouraging better practices than validation. That also means though that they are easier for users to ignore. Check in with your users every once and a while to see if they actually find help messages useful and think carefully about how many you use.

---

That's all of the code that was included in the PyLadiesCon talk. But we're going to include a Bonus Step 6 here so that you can learn more about the Wagtail accessibility checker and how that can also be a useful tool for promoting accessibility. (https://github.com/vossisboss/pyladiescon2025/tree/step-6).
