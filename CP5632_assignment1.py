__author__ ="Jorie Gomez"

# Initialize the constants
BOOK_FILE = "books.csv"

def main():
	print("Reading List 1.0 - by Jorie Gomez")
	book_list = []
	load_books(book_list)
	display_menu()

	choice = input('>>> ')
	choice = choice.upper()

	while choice != 'Q':
		if choice == 'R':
			list_required_books(book_list)
		elif choice == 'C':
			list_completed_books(book_list)
		elif choice == 'A':
			add_new_books(book_list)
		elif choice == 'M':
			mark_book_completed(book_list)
		else:
			print('Please enter R, C, A, M or Q(uit')
		display_menu()
		choice = input('>>> ').upper()
		print('Have a nice day :)')

# end of main()


def load_books(book_list):
	"""

	"""

# end of load_books()

def display_menu():
	print('R - List required books')
	print('C - List completed books')
	print('A - Add new book')
	print('M - Mark a book as completed')
	print('Q - Quit')


#def load_books(book_list):
	"""


	"""
print("load books")

# end of load_books()

def list_required_books(book_list):
	print('list_required_books')

def list_completed_books(book_list):
	print('list_completed_books')

def add_new_books(book_list):
	print('add_new_books')

def mark_book_completed(book_list):
	print('mark_book_completed')

def complete_a_book():
	"""


	"""

print("complete a book")

# end of complete_a_book()

# Start the program
main()
