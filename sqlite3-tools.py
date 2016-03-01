#!/usr/bin/env python
# -*- coding: utf-8 -*-
# CL Simplex 2015
# https://CLSimplex.com
#
# Free Beer License.
# 'As is'.
# Don't expect anything from this. At all. Seriously.

import os
import tablib
import subprocess
import sqlite3 as sql

def sqlite3_table_to_xls(database_path, table_name, export_path):
	"""
	Given an sqlite3 database file and a table_name, export it to a spreadsheet.
	No sanity checks included.
	"""

	connection = sql.connect( database_path )
	cursor = connection.cursor()
	cursor.execute( 'SELECT * FROM ' + str(table_name) )

	col_names = [cn[0] for cn in cursor.description]

	rows = cursor.fetchall()

	data = tablib.Dataset()

	data.headers = col_names

	for item in rows:
		data.append(item)

	full_export_path = str(export_path) + str(table_name) + '_export.xls'

	print('Creating xls sheet at: ' + str(full_export_path))

	file_handler = open( full_export_path, 'wb+' )
	file_handler.write(data.xls)

	file_handler.close()
	connection.close()



def sqlite3_table_entries_by_git_commit_history(repo_path, database_path, table_name, commits=20):
	"""
	Given a repo, a database_path, and a table_name - display the number of entries in the table going back COMMITS commits.
	This assumes you have GIT installed as well as a local repo of whatever you are attemping to look at.

	Returns a list of tuples of the form (COMMITS BACK, ROWS)

	This uses checkout_output with shell=True so be careful with this one.
	"""
	new_database_path = '/var/tmp/database.db'

	original_cwd = os.getcwd()

	os.chdir(repo_path)

	commits_back = commits

	results = []

	while commits_back > -1:
		git_command = 'git show HEAD~' + str( commits_back ) + ':.' + str( database_path )

		# Given git output, write a new, temporary file.
		file_pointer = open( new_database_path, 'wb+')

		output = subprocess.check_output( git_command, shell=True )

		file_pointer.write( output )
		file_pointer.close()

		connection = sql.connect( new_database_path )

		cursor = connection.cursor()

		cursor.execute( 'SELECT * FROM ' + str( table_name ) )

		rows = cursor.fetchall()

		results.append((commits_back,rows))
	
		commits_back = commits_back - 1
		connection.close()

	os.chdir(original_cwd)

	return results