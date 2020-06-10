#!/usr/bin/env python3

import os
import os.path
import sys
import yaml


def get_nav_paths():
    """Load all paths from navigation.yml"""
    nav = yaml.load(open('./_data/navigation.yml'), Loader=yaml.SafeLoader)

    def _get_paths(el):
        ret = []
        if 'url' in el:
            ret.append(el['url'])
        for c in el.get('children', []):
            ret.extend(_get_paths(c))
        return ret

    ret = []
    for e in nav['main']:
        ret.extend(_get_paths(e))
    return ret


def valid_path(p):
    """Check path."""
    _, ext = os.path.splitext(p)
    return ext in ('.md', '.html')


def translate_path(p):
    """Translate path."""
    # strip prefix
    pfx = "_kb"
    if p[:len(pfx)] == pfx:
        p = p[len(pfx):]
    head, tail = os.path.split(p)
    if tail in ('index.md', 'index.html'):
        return head
    name, _ = os.path.splitext(tail)
    return os.path.join(head, name)


def contains_dupes(pathset):
    return len(set(pathset)) != len(pathset)


def get_file_paths():
    """Get all paths from kb."""
    ret = []
    for dirname, _, files in os.walk('_kb'):
        fullfiles = [os.path.join(dirname, f) for f in files]
        ret.extend(fullfiles)
    return [translate_path(f) for f in ret if valid_path(f)]


def main():
    navs = get_nav_paths()
    #print(navs)
    paths = get_file_paths()
    if contains_dupes(paths):
        print('Warning: Duplicates in Paths!')
        sys.exit(1)
    missing = set(paths) - set(navs)
    if missing:
        print('Missing paths from nav:')
        for p in sorted(missing):
            print('-- {}'.format(p))
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    main()
