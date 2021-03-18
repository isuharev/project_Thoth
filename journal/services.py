# 24.11.2020
# Если этот код работает, то его написал Сухарев-Крылов И.А., а если нет, то я не знаю, кто его написал

# Данный импорт нужен просто для удобства, чтобы отобразить тип возвращаемого значения для одной из функций ниже
import django.db.models.query as query


def get_next_number(obj, department) -> int:
    """
    Эта функция позволяет получить следующий номер по порядку для новой регистрационной записи в журнале
    :param obj: объект формы, содержащий все её поля
    :param department: переменная типа str, содержащая в себе название отдела,
                                                                к которому будет привязан регистрируемый документ
    :return: целочисленное значение номера для создаваемой записи
    """
    # Зададим номер по умолчанию
    number = 0

    for i in obj.objects.all().order_by('-id'):
        if str(i.departament).strip().lower() == str(department).strip().lower():
            number = i.number + 1
            break

    return number


def get_new_number_out(obj, request) -> str:
    """
    Эта функция определяет значение поле "№ Исх." для новой записи в журнале
                                                                        на основе последней записи для данного отдела.
    :param request: POST запрос от пользователя
    :param obj: объект формы, содержащий все её поля
    :return: строковое значение поля "№Исх."
    """
    current = "TEST!"
    # Проверим, состоит ли пользователь в каком либо отделе
    # Если состоит, то будем искать последний № Исх. для данного отдела в базе
    # Если пользователь состоит в нескольких отделах, то отделом по умолчанию будем считать первый указанный
    # Если не состоит, то вернём пустую строку

    if request.user.groups.all():

        department = request.user.groups.all()[0]

        for entry in obj.objects.all().order_by('-id'):
            if str(entry.departament).strip().lower() == str(department).strip().lower():

                if "-" in str(entry.number_out):
                    # Если нам попался № Исх. нового образца вида "N-M/K", то приводим его в виду "N/K"
                    # После чего приводим к виду "N/K+1", чтобы получился № Исх. для записи, которую создают сейчас
                    number_out = str(entry.number_out).split("-")
                    current = number_out[0] + '/'\
                        + str(int(number_out[1].split("/")[1]) + 1)

                else:
                    # Если же попался № Исх. старого образца, вида "N/K", то приводим сразу к виду "N/K+1"
                    current = str(entry.number_out).split("/")[0]\
                              + "/"\
                              + str(int(str(entry.number_out).split("/")[1]) + 1)
                break
        else:
            if str(department).strip().lower() == "гравиметрии":
                current = "152/"
            elif str(department).strip().lower() == "геодинамики":
                current = "155/"
            elif str(department).strip().lower() == "тестеры":
                current = "Тестовый/"
    return current


def get_department_name(obj, request) -> str:
    """
    Эта функция определяет отдел,
        для которого зарегистрировали новый документ по номеру отдела в поле "№Исх." или по группе самого пользователя
    :param obj: объект формы, содержащий все её поля
    :param request: POST запрос от пользователя
    :return: название отдела для новой записи в журнале
    """
    # Научим сайт определять отдел по префиксу исходящего номера
    chk = obj.number_out.split("/")
    if chk[0] == "155":
        return "Геодинамики"
    elif chk[0] == "152":
        return "Гравиметрии"
    else:
        # Если по префиксу распознать не удаётся, то пробуем считать название отдела по имени группы
        try:
            return request.user.groups.get().name
        except:
            # Если группа не указана, присвоим значение по умолчанию
            return "не указан"


def get_some_last_model_elements(obj, begin: int, end: int) -> query.QuerySet:
    """
    Эта простенькая функция возвращает элементы заданной модели, заключённые в промежутке от begin до end
    :param obj: данная модель
    :param begin: целое число, индекс, с которого начинается выборка
    :param end: целое число, индекс, с которого заканчивается выборка
    :return: queryset с количеством элементов от begin до end
    """
    return obj.objects.all().order_by('-id')[begin:end]
