from wagtail import hooks
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup

from home.models import Service, FeatureTab

class FeatureTabSnippetView(SnippetViewSet):
    model = FeatureTab
    menu_label = 'Tabs'
    menu_icon='folder-open-inverse'
    menu_order=310


class ServiceSnippetView(SnippetViewSet):
    model = Service
    menu_label = 'Icon Items'
    icon = 'icon'
    menu_order=320

class SiteComponentsViewSetGroup(SnippetViewSetGroup):
    menu_label = 'Site Components'
    menu_icon = 'placeholder' 
    menu_order = 300 
    items = (ServiceSnippetView, FeatureTabSnippetView)

register_snippet(SiteComponentsViewSetGroup)