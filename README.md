# ansible-role-mkdocs_i18n

This Ansible role scaffolds a multilingual [MkDocs](https://www.mkdocs.org/) website using the [Material theme](https://squidfunk.github.io/mkdocs-material/) with full support for [mkdocs-static-i18n](https://github.com/lukasgeiter/mkdocs-static-i18n).

## Features

- Fully static, multilingual documentation scaffold
- Automatic slugification of navigation labels using a custom `build_nav_entry` filter
- Consistent directory structure for all languages, including the default
- Automatically generates `mkdocs.yml`, navigation entries, and scaffolded content
- Compatible with Ansible 2.13+
- No dependency on `community.general`

## Example Usage

### Minimal Playbook

```yaml
- hosts: localhost
  gather_facts: false
  roles:
    - role: mkdocs_i18n
```

### Example Configuration (`defaults/main.yml`)

```yaml
mkdocs_site_name: "example.com"
mkdocs_site_dir: "~/projects/sites/dev/{{ mkdocs_site_name }}"
mkdocs_config_file: "mkdocs.yml"
mkdocs_docs_dir: "docs"
mkdocs_output_dir: "site"

mkdocs_languages:
  - code: "en"
    name: "English"
    default: true
    nav:
      - name: "Home"
      - name: "About"
      - name: "Contact"
  - code: "fr"
    name: "Français"
    nav:
      - name: "Accueil"
      - name: "À propos"
      - name: "Contact"

mkdocs_theme_name: "material"
mkdocs_plugins:
  - search
  - i18n
```

## Language Requirements

Each language entry in `mkdocs_languages` must:

- Define a `code`, `name`, and list of `nav` items
- Include exactly **one** language marked as `default: true`
- Include **at least one** navigation item
- Ensure the **first nav item** represents that language’s homepage

These values are required to correctly generate navigation structure and create a working redirect from `docs/index.md` to the proper homepage for the default language.

## Slugification: `build_nav_entry` and `semantic_slug`

This role includes a custom Ansible filter plugin defined in:

```
filter_plugins/mkdocs_helpers.py
```

It exposes two filters:

- `semantic_slug(value)` – Normalizes a single string into a clean, URL-safe slug
- `build_nav_entry(name, code)` – Takes a page name and language code and returns a structured object with:

```yaml
- name: "À propos"
  slug: "a-propos"
  code: "fr"
```

The `build_nav_entry` filter is used in the role to generate slugified nav structures. It internally uses `semantic_slug`, which:

- Normalizes Unicode (e.g., removes accents)
- Converts to lowercase
- Replaces whitespace with hyphens
- Removes punctuation

Example conversions:

| Label              | Slug               |
|--------------------|--------------------|
| `À propos`         | `a-propos`         |
| `Nos réalisations` | `nos-realisations` |

## Generated Directory Structure

All content is generated inside `docs/<language_code>/`, including the default language. While the `mkdocs-static-i18n` plugin recommends placing the default language content at the root of `docs/`, this role uses a consistent folder structure across all languages.

The plugin will still render the default language at the site root (e.g., `site/about/`), while other languages will be rendered to subdirectories (e.g., `site/fr/a-propos/`).

Example output:

```shell
docs/
├── en/
│   ├── home/
│   │   └── index.md
│   ├── about/
│   │   └── index.md
│   └── contact/
│       └── index.md
├── fr/
│   ├── accueil/
│   │   └── index.md
│   ├── a-propos/
│   │   └── index.md
│   └── contact/
│       └── index.md
```

## Compatibility

- Tested with Ansible 2.13+
- No external Python packages required
- No community collections used

MIT License • Built with care