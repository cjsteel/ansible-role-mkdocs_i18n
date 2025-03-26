# ansible-role-mkdocs_i18n

This Ansible role scaffolds a multilingual [MkDocs](https://www.mkdocs.org/) website using the Material theme with full support for [mkdocs-static-i18n](https://github.com/lukasgeiter/mkdocs-static-i18n).

## Features

- Fully static, multilingual documentation scaffold
- Automatic slugification of navigation labels via a custom `semantic_slug` filter
- Consistent directory structure for all languages, including the default
- No dependency on `community.general`
- Compatible with Ansible 2.13+

## Example Usage

### Playbook

```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: mkdocs_i18n
```

### Defaults

The latest role defaults are maintained in [defaults/main.yml](./defaults/main.yml).

## Slugification: `semantic_slug`

This role includes a custom filter plugin, `semantic_slug`, which:

- Normalizes Unicode (e.g., removes accents)
- Converts to lowercase
- Replaces whitespace and underscores with hyphens
- Removes punctuation
- Produces clean, URL-friendly slugs

| Label              | Slug               |
|--------------------|--------------------|
| `À propos`         | `a-propos`         |
| `Nos réalisations` | `nos-realisations` |

## Generated Structure

By default, the role places all language content inside `docs/<language_code>/`, including the default language. This contrasts with the plugin maintainer’s recommendation to place default language content at the root of `docs/`.

This deviation is deliberate — it ensures a consistent structure for automation and maintenance. If the plugin maintainers eventually remove support for this layout, the role may need to be updated.

Example output:

```
docs/
├── en/
│   ├── about/
│   │   └── index.md
│   ├── contact/
│   │   └── index.md
│   └── welcome/
│       └── index.md
├── fr/
│   ├── a-propos/
│   │   └── index.md
│   ├── contact/
│   │   └── index.md
│   └── accueil/
│       └── index.md
```

## Compatibility

- Tested with Ansible 2.13+
- No external Python packages required
- No community collections used

## Plugin: `semantic_slug`

Located in `filter_plugins/mkdocs_helpers.py`, this filter is automatically loaded when the role runs. It ensures all generated paths and directory names are clean and web-safe.

---

MIT License • Built with care
