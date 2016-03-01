# SQLITE3 TOOLS
These are some tools we once needed. This is our very tiny way of giving
back to the open source community.

We hope these incredibly specific (and possibly broken - it has been a while) functions can help you.
## LICENSE
`AS IS` and `FREE BEER` licenses. We promise nothing and expect as much back in return.
## COLLABORATION
We have no policy or plan to continue to work on these tools. This may change, it may not.
We may ignore any issues, or we may work to fix them. Depends of everything, really.

### Requirements
Refer to `requirements.txt`

# sqlite3_table_to_xls
This function gets a single table from within an sqlite3 database and exports
it to an xls format.
## Usage
All parameters are strings. Return is **void**.

sqlite3_table_to_xls( database_path, table_name, export_path )

*Example:* sqlite3_table_to_xls( '/path/to/sqlite3.db', 'store_Product', '/path/to/export/' )

/path/to/sqlite3.db's 'store_Product' table will be exported to `/path/to/export/store_Product_export.xls`.

# sqlite3_table_entries_by_git_commit_history
This verbosely named function retrieves the number of entries a table has contained throughout a git repo's history.
Funny story, I once nuked the sqlite3 database in a django project and I needed to find the commit that had the original entries.
## Usage
All mandatory parameters are strings. Returns a **list of tuples**

sqlite3_table_entries_by_git_commit_history(repo_path, database_path, table_name, commits=20)

*Example:* sqlite3_table_entries_by_git_commit_history( '/path/to/repo', '/relative/db/path/sqlite3.db', 'store_Product' )

(COMMITS_BACK, ROWS)

COMMITS_BACK refers to how far back we currently are from the HEAD of the repo.

### Further Documentation
Unfortunately, this is all the documentation I'm willing to type at the moment.
If you need more information contact us. Please bear in mind addressing
these issues are of low priority to us.