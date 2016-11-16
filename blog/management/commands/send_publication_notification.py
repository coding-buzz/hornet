from django.core.management.base import BaseCommand
from django.conf import settings
from django.template.loader import get_template

from mailchimp3 import MailChimp

from blog.models import BlogPost


class Command(BaseCommand):
    
    _CLIENT = MailChimp('', settings.MAILCHIMP_API_KEY)
    _NOTIFICATION_TEMPLATE = 'blog/mailer/publication_notification.html'
    _REPLY_TO = 'no-reply@coding.buzz'

    def add_arguments(self, parser):
        parser.add_argument('blog_post_id', type=int)
    
    def handle(self, *args, **options):
        if not settings.MAILCHIMP_SEND_EMAILS:
            print 'Skipping blog post publication notification because MAILCHIMP_SEND_EMAILS flag is set to False.'
            return
        blog_post_id = options['blog_post_id']
        blog_post = BlogPost.objects.get(id=blog_post_id)
        campaign_id = self._create_campaign(blog_post)
        self._update_campaign_html(campaign_id, blog_post)
        self._CLIENT.campaigns.actions.send(campaign_id=campaign_id)
        print 'Blog post {} publication notification has been sent.'.format(blog_post_id)

    def _create_campaign(self, blog_post):
        mailing_list_id = self._get_mailing_list_id()
        resp = self._CLIENT.campaigns.create(data={
            'type': 'regular',
            'recipients': {
                'list_id': mailing_list_id
            },
            'settings': {
                'subject_line': 'Coding Buzz | {}'.format(blog_post.title),
                'from_name': 'Coding Buzz',
                'reply_to': self._REPLY_TO
            }
        })
        campaign_id = resp['id']
        return campaign_id

    def _get_mailing_list_id(self):
        lists = self._CLIENT.lists.all()['lists']
        list_id = filter(lambda x: x['name'] == settings.MAILCHIP_SUB_LIST_NAME, lists)[0]['id']
        return list_id

    def _update_campaign_html(self, campaign_id, blog_post):
        html_content = self._get_campaign_html(blog_post)
        self._CLIENT.campaigns.content.update(campaign_id=campaign_id, data={
            'html': html_content
        })

    def _get_campaign_html(self, blog_post):
        template = get_template(self._NOTIFICATION_TEMPLATE)
        html_content = template.render(context = {
            'BASE_URL': settings.BASE_URL,
            'blog_post': blog_post
        })
        return html_content
