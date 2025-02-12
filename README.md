## Установка и запуск

- **0.** Предварительно необходимо скачать с официального сайта (https://git-scm.com/download/win) и установить на компьютере "Git Bash".

   Для корректной работы желательно произвести предварительную настройку "Git Bash", согласно руководству с оф. сайта (https://git-scm.com/book/ru/v2/Введение-Первоначальная-настройка-Git).

- **1.** Предварительно необходимо скачать с официального сайта (https://www.python.org/) и установить на компьютер `Python` (версию не ниже 3.13.1)

- **2.** Клонируйте репозиторий:
   Запустите "Командную строку".
   
    - 1.1. Введите в строке команду:

    `git clone https://github.com/niknikas24/pytest.git`

- **3.** Предварительная настройка:

    - 3.1. Обычно `pip` предустанавливается вместе с `Python`. Для проверки, нужно открыть «Командную строку» и ввести (для Windows):

    `py -m ensurepip --upgrade`

    - 3.2. Когда `pip` установлен, для установки модуля `requests` нужно ввести в «Командную строку»:

    `pip install requests`

    - 3.3. Теперь нам нужно установить `pytest`, вводим в «Командную строку»:
    
    `pip install pytest==8.3.4`  

    - 3.4. Затем устанавливаем `pluggy`, вводим в «Командную строку»:

    `pip install pluggy==1.5.0` 

- **4.** Теперь можно перейти к самим тестам. Запустите на компьютере "Командную строку":

    - 4.1. Введите в строке команду:

    `cd C:\Users\current_user_name\pytest`

    `Примечание: вместо "current_user_name" - нужно вписать имя текущего пользователя компьютера!`  

    - 4.2. Произвести постепенный запуск в строке команд:
 
    `pytest test_pet.py`

    `pytest test_user.py`

    `pytest test_store.py`
