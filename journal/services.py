# 24.11.2020
# Если этот код работает, то его написал Сухарев-Крылов И.А., а если нет, то я не знаю, кто его написал


def get_current_number(obj):
    return obj.objects.all().order_by('-id')[0].number + 1


def get_current_number_out(obj):
    return obj.objects.all().order_by('-id')[0].number_out


def get_department_name(obj, request):
    """
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


def get_some_last_model_elements(obj, begin: int, end: int):
    """
    Эта простенькая функция возвращает элементы заданной модели, заключённые в промежутке от begin до end
    :param obj: данная модель
    :param begin: целое число, индекс, с которого начинается выборка
    :param end: целое число, индекс, с которого заканчивается выборка
    :return: queryset с количеством элементов от begin до end
    """
    return obj.objects.all().order_by('-id')[begin:end]
