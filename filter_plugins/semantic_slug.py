import unicodedata
import re
from ansible.errors import AnsibleFilterError


def semantic_slug(value):
    if not isinstance(value, str):
        raise AnsibleFilterError("semantic_slug expects a string input")

    # Normalize unicode (decompose accented characters)
    value = unicodedata.normalize('NFKD', value)
    value = value.encode('ascii', 'ignore').decode('utf-8')

    # Lowercase and strip whitespace
    value = value.strip().lower()

    # Remove all non-alphanumeric characters except spaces and hyphens
    value = re.sub(r'[^\w\s-]', '', value)

    # Replace spaces and underscores with hyphens
    value = re.sub(r'[\s_]+', '-', value)

    # Collapse multiple hyphens
    value = re.sub(r'-{2,}', '-', value)

    # Remove leading/trailing hyphens
    return value.strip('-')


class FilterModule(object):
    def filters(self):
        return {
            'semantic_slug': semantic_slug
        }
