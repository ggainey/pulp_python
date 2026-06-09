# Package Policies

Python repositories offer two mechanisms for controlling which packages they accept:
**blocklists** to prevent specific packages from being added, and
**package substitution control** to prevent silent replacement of existing packages.

## Setup

If you do not already have a repository, create one:

```bash
pulp python repository create --name foo
```

## Package Blocklist

A repository can have a blocklist that prevents specific packages from being added.
Blocklist entries can match by package `name` (blocks all versions), package `name` with an exact `version`, or exact `filename`.
Exactly one of `name` or `filename` must be provided.

Package `name` is normalized using [PEP 503](https://peps.python.org/pep-0503/) before being stored, 
and `version` must follow [PEP 440](https://peps.python.org/pep-0440/) rules.

Each entry records the PRN of the user who created it in the `added_by` field.

### Add a blocklist entry

=== "By name"

    ```bash
    # Block all versions of shelf-reader
    pulp python repository blocklist add --repository "foo" --name "shelf-reader"
    ```

=== "By name and version"

    ```bash
    # Block only shelf-reader 0.1
    pulp python repository blocklist add --repository "foo" --name "shelf-reader" --version "0.1"
    ```

=== "By filename"

    ```bash
    # Block only shelf-reader-0.1.tar.gz
    pulp python repository blocklist add --repository "foo" --filename "shelf-reader-0.1.tar.gz"
    ```

### List blocklist entries

```bash
pulp python repository blocklist list --repository "foo"
```

### Show a blocklist entry

=== "By name"

    ```bash
    pulp python repository blocklist show --repository "foo" --name "shelf-reader"
    ```

=== "By name and version"

    ```bash
    pulp python repository blocklist show --repository "foo" --name "shelf-reader" --version "0.1"
    ```

=== "By filename"

    ```bash
    pulp python repository blocklist show --repository "foo" --filename "shelf-reader-0.1.tar.gz"
    ```

### Remove a blocklist entry

=== "By name"

    ```bash
    pulp python repository blocklist remove --repository "foo" --name "shelf-reader"
    ```

=== "By name and version"

    ```bash
    pulp python repository blocklist remove --repository "foo" --name "shelf-reader" --version "0.1"
    ```

=== "By filename"

    ```bash
    pulp python repository blocklist remove --repository "foo" --filename "shelf-reader-0.1.tar.gz"
    ```

Once an entry is removed, packages matching it can be added to the repository again.

## Package Substitution

By default, Python repositories allow package substitution: uploading, syncing, or adding a package
with the same filename as an existing package but a different checksum will silently replace it.

This behavior is controlled by the `allow_package_substitution` field on a Python repository.
When set to `False`, any operation (upload, sync, or modify) that would replace an existing package with a different checksum is rejected.
Re-adding a package with the same filename *and* the same checksum is always accepted (idempotent).

### Disable package substitution

```bash
pulp python repository update --repository "foo" --block-package-substitution
```

You can also set this when creating a repository:

```bash
pulp python repository create --name "foo2" --block-package-substitution
```

### Re-enable package substitution

```bash
pulp python repository update --repository "foo" --allow-package-substitution
```

Once re-enabled, packages with duplicate filenames can replace existing content again.
