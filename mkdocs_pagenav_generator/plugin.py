from mkdocs.plugins import BasePlugin
from mkdocs.utils import normalize_url


class NavGeneratorPlugin(BasePlugin):

    def on_nav(self, nav, config, files):
        self.nav = nav

    def on_post_page(self, output, page, config):
        if '{nav}' in output:
            children = page.parent.children if page.parent else self.nav.items
            siblings = [child for child in children if child is not page]
            return output.replace('{nav}', self._format_links(siblings, page, config))

    def _format_links(self, items, page, config):
        result = '<ul>'

        for item in items:
            result += '<li>'

            if item.is_section:
                result += item.title
                result += self._format_links(item.children, page, config)
            else:
                url = normalize_url(item.url, page)
                result += f'<a href="{url}">{item.title}</a>'

            result += '</li>'

        result += '</ul>'

        return result
