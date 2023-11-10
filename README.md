# MathSnapApp: Решение уравнений с использованием изображений

## Введение

**MathSnapApp** - это приложение, предназначенное для решения уравнений с изображений с рукописным вводом. Проект объединяет в себе несколько ключевых компонентов, обеспечивая простоту использования, точность распознавания и удобный интерфейс для пользователя.

<div style="display: flex; flex-direction: row;">
    <img src="https://i.imgur.com/EirN3hF.png" alt="Изображение 1" style="width: auto; height: 500px; margin-right: auto;">
</div>


## Как это работает

### 1. Интерфейс

Главное окно приложения содержит две основные функциональности:

- **История решений**: Позволяет пользователю просматривать историю решенных уравнений.

<div style="display: flex; flex-direction: row;">
    <img src="https://i.imgur.com/b0IuBKd.png" alt="Изображение 2" style="width: auto; height: 500px; margin-right: auto;">
</div>


- **Решение уравнения**: Позволяет пользователю загружать изображения уравнениями для их решения.
<div style="display: flex; flex-direction: row;">
    <img src="https://i.imgur.com/DuwBsen.png" alt="Изображение 3" style="width: auto; height: 500px; margin-right: auto;">
</div>

### 2. Модуль Parser

Модуль `parser.py` отвечает за обработку изображений с рукописными уравнениями. Он использует внешний ресурс (OCR API от Mathway) для распознавания текста на изображении. Полученное уравнение затем передается модулю `reshatel.py` для решения.

### 3. Модуль Reshatel

Модуль `reshatel.py` выполняет фактическое решение уравнения. Он использует библиотеку `sympy`, чтобы представить уравнение и вычислить его корни. Результаты передаются обратно в основной код для дальнейшего отображения.

### 4. Модуль Database

Модуль `database.py` управляет базой данных SQLite (`history.db`), где хранится история уравнений и их решений. Он предоставляет методы для добавления, извлечения и очистки данных.

### 5. Модуль Result UI

Модуль `result_ui.py` отвечает за графическое отображение результатов решения уравнения. В зависимости от наличия изображения, также отображается само уравнение.

### 6. Модуль Translating

Модуль `translating.py` используется для перевода текста, в данном случае, для обработки сообщений об ошибках или предупреждений.

### 7. Упаковка приложения

Файл `setup.py` содержит информацию для упаковки приложения с использованием `py2app`. 

## Преимущества проекта

- **Простота использования**: Пользовательский интерфейс разработан с учетом интуитивной навигации.

- **Точность распознавания**: Использование внешнего ресурса Mathway для распознавания текста обеспечивает высокую точность.

- **История решений**: Пользователи могут в любой момент просматривать свою историю решенных уравнений.

- **Гибкость**: Проект легко расширяем и может быть адаптирован для использования с другими библиотеками или сервисами.

## Заключение

**MathSnapApp** представляет собой мощный инструмент для решения уравнений, который сочетает в себе передовые технологии распознавания с интуитивно понятным пользовательским интерфейсом. Будучи легко настраиваемым и легким в использовании, проект предоставляет решение для тех, кто ищет удобный способ решения математических задач.

---

## Установка на Windows или Linux
Для установки приложения выполните следующие шаги:

Убедитесь, что у вас установлен Python.

Установите необходимые библиотеки, запустив команду:

`pip install -r requirements.txt`

Запустите приложение:

`python main.py`

---

## Установка на MacOs
Для MacOs существует скомпилированная версия (.app). Для того, чтобы установить её, нажмите на [данную ссылку](https://drive.google.com/uc?export=download&id=1NktlAoCE-T1kWBuTh-kz5yY9AxBwM9G0), а затем разархивируете файл `main.app.zip`.
