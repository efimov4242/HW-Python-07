import model
import view

model.read_db('database.txt')


def input_handler(inp: int):
	match inp:
		case 1:
			view.show_all(model.db_list)
		case 2:
			model.read_db('database.txt')

while True:
	user_inp = view.main_menu()
	input_handler(user_inp)