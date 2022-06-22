# file_cleaner
A simple Python script to recursively clean temporary files with a given extension.

Default behaviour is to remove the `*.mem` files created by the Julia profiler, but the extension can be configured easily in the script.

Usage:

`python mem_cleaner.py .`

The command above will preview the files to be removed in the current path (a different path may be specified). To actually carry out the deletion of those files, execute the operation with:

`python mem_cleaner.py . -e`

No guarantee of any kind is provided: the user is fully responsible for ensuring that the script does not carry out unintended deletions.
