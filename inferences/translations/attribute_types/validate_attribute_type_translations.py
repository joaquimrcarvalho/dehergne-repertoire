#!/usr/bin/env python3
"""Validate attribute type translations.

Ensure all base items are present in the English file and that
ambiguous entries are marked with '*' when they were kept as the
original string.

Usage:
    python validate_attribute_type_translations.py \
        --base attribute_type_base.csv \
        --en attribute_type_EN.csv \
        [--fix] [--whitelist dehergne,geoentity:name@geonames,...]

Options:
    --fix
        Prefix '*' for ambiguous entries in the EN file where the
        translation equals the base string.
    --whitelist
        Comma-separated list of keys (attribute_type) where identity is
        expected (i.e. translations should be identical to the base).

The script exits with 0 on success. If issues were found the exit
code is non-zero, unless --fix is used and fixes were applied.
"""

import argparse
import csv
import shutil
import sys
from pathlib import Path


def load_csv(file_path):
    """Load a CSV with 'attribute_type' and 'attribute_type_copy'.

    Returns a dict keyed by attribute_type with the translated value.
    """
    items = {}
    with open(file_path, newline='', encoding='utf-8') as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            items[row['attribute_type']] = row['attribute_type_copy']
    return items


def write_csv(file_path, rows):
    """Write a two-column CSV for attribute_type translations.

    'rows' should be an iterable of (key, value) pairs.
    """
    with open(file_path, 'w', newline='', encoding='utf-8') as fh:
        writer = csv.writer(fh)
        writer.writerow(['attribute_type', 'attribute_type_copy'])
        for key, val in rows:
            writer.writerow([key, val])


def main():
    parser = argparse.ArgumentParser(
        description='Validate attribute type translations',
    )
    parser.add_argument(
        '--base',
        default='attribute_type_base.csv',
        help='Path to base CSV',
    )
    parser.add_argument(
        '--en',
        default='attribute_type_EN.csv',
        help='Path to EN CSV (translation)',
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Auto-fix ambiguous entries by adding "*" prefix',
    )
    parser.add_argument(
        '--whitelist',
        default='',
        help=('Comma-separated list of attribute_type keys allowed to be '
              'identical'),
    )

    args = parser.parse_args()

    base_path = Path(args.base)
    en_path = Path(args.en)

    if not base_path.exists():
        print(f"ERROR: base file not found: {base_path}")
        sys.exit(2)
    if not en_path.exists():
        print(f"ERROR: en file not found: {en_path}")
        sys.exit(2)

    # Default whitelist: tokens that are expected to remain the same
    # across locales or be language-neutral identifiers.
    DEFAULT_WHITELIST = {
        'alternative-name',
        'alternative-name@wikidata',
        'dehergne',
        'dehergne@archive',
        'geoentity:name@dehergne',
        'geoentity:name@geonames',
        'geoentity:name@wikidata',
        'historical-source:id@dehergne',
        'note',
        'person:id@bdcconline',
        'wicky',
    }
    # Build the user whitelist from CLI args (if any).
    user_whitelist = set()
    if args.whitelist:
        vals = [x.strip() for x in args.whitelist.split(',') if x.strip()]
        user_whitelist = set(vals)
    whitelist = user_whitelist | DEFAULT_WHITELIST

    base_items = load_csv(base_path)
    en_items = load_csv(en_path)

    missing_in_en = []
    identical_unmarked = []
    starred_but_changed = []
    blank_values = []

    for key, base_val in base_items.items():
        if key not in en_items:
            missing_in_en.append((key, base_val))
            continue
        en_val = en_items[key]
        if en_val == '':
            blank_values.append((key, base_val, en_val))
        if (
            en_val == base_val and
            not en_val.startswith('*') and
            key not in whitelist
        ):
            identical_unmarked.append((key, base_val, en_val))
        # If it starts with '*' and differs from base,
        # treat it as a changed translation
        if (
            en_val.startswith('*') and
            en_val.lstrip('*') != base_val and
            key not in whitelist
        ):
            starred_but_changed.append((key, base_val, en_val))

    has_issues = bool(missing_in_en or identical_unmarked or blank_values)

    print('Validation summary:')
    print('  Base rows:', len(base_items))
    print('  EN rows:  ', len(en_items))
    print()

    if missing_in_en:
        print('Missing keys in EN file:')
        for key, val in missing_in_en:
            print('  ', key, '|', val)
        print()

    if identical_unmarked:
        print('Identical (unmarked) entries (should be starred if ambiguous):')
        for key, base_val, en_val in identical_unmarked:
            print('  ', key, '|', base_val)
        print()

    if blank_values:
        print('Entries with blank translation value:')
        for key, base_val, _ in blank_values:
            print('  ', key, '|', base_val)
        print()

    if starred_but_changed:
        print('Entries that are starred and changed:')
        for key, base_val, en_val in starred_but_changed:
            print('  ', key, '| base:', base_val, '| en:', en_val)
        print()

    if args.fix and identical_unmarked:
        print('\nApplying fixes: prefixing "*" to ambiguous entries...')
        backup_path = en_path.with_suffix('.csv.bak')
        shutil.copy(en_path, backup_path)
        # Apply fixes if requested.
        updated_rows = []
        with open(en_path, newline='', encoding='utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                key = row['attribute_type']
                val = row['attribute_type_copy']
                if key in dict((k, b) for (k, b, e) in identical_unmarked):
                    val = '*' + val
                updated_rows.append((key, val))
        write_csv(en_path, updated_rows)
        print('Backup written to', backup_path)
        print('EN file updated.')
        # re-run validation to show results
        print('\nRe-running validation...')
        return_code = 0

        # read again to get current status
        en_items = load_csv(en_path)
        # check still any identical
        left_identical = []
        for key, base_val in base_items.items():
            if key in en_items:
                val = en_items[key]
                if (
                    val == base_val and
                    not val.startswith('*') and
                    key not in whitelist
                ):
                    left_identical.append(key)
        if left_identical:
            print('Remaining unstarred identical entries:', left_identical)
            return_code = 3
        else:
            print('All ambiguous identical entries were starred.')
            return_code = 0
        return return_code

    if has_issues:
        print('\nValidation FAILED: found issues listed above.')
        return 1
    else:
        print('\nValidation OK: No issues found.')
        return 0


if __name__ == '__main__':
    sys.exit(main())
