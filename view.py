def main_menu() -> int:
	print('Главное меню: ')
	menu_list = [
					 'Показать все контакты',
					 'Открыть файл',
					 'Сохранить файл',
					 'Создать контакт',
					 'Изменить контакт',
					 'Удалить контакт',
					 'Выход'
					]

	for i in range(len(menu_list)):
		print(f'   {i+1}. {menu_list[i]}')
	user_input = int(input('Введите команду :> '))
	return user_input

def show_all(db: list):
	if len(db) < 1:
		print('Телефонная книга пуста')
	else:
		for i in range(len(db)):
			user_id = i + 1
			print(f'\t{user_id}', end = ". ")
			for v in db[i].values():
				print(f'{v}', end = " ")
			print()

def db_success(db: list):
	if db:
		print('Телефонная книга открыта')
	else:
		print('Телефонная книга пуста или не открыта')
