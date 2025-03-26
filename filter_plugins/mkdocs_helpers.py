import unicodedata
import re

def semantic_slug(value):
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('utf-8')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[\s]+', '-', value)

def build_nav_entry(name, code):
    return {
        "name": name,
        "slug": semantic_slug(name),
        "code": code
    }

class FilterModule(object):
    def filters(self):
        return {
            "semantic_slug": semantic_slug,
            "build_nav_entry": build_nav_entry
        }
