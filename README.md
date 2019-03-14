# test_user
Homework Django User 

<p>Models.py</p> 

Создана расширенная модель пользователя, дабавлены поля: second_name, birth_date, created_at, update_at, auth_key.
Созданы методы вывода инициалов, полного ФИО, возраста пользователя

<p>Forms.py</p>

Созданы формы создания, изменения, логина пользователя

<p>Views.py</p>

Описаны методы регистрации, изменения данных, удаления, аутентификации, выхода из системы, восстановления пароля.

<p>Test.py</p>

test_age - проверка функции подсчета возраста
test_registration_template - получение страницы пользователем
test_user_creation - создании записи в базе данных при регистрации
test_registration - проверка ввода данных пользователем, валидности формы регистрации, пробелов в полях
test_login - проверяет статус is_active при авторизации
test_edit_template - получение шаблона изменения данных
test_validate_input - валидность формы, созранение данных в бд
