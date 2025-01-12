def validar_datos(datos):
    """
    Проверка данных на противоречия.
    """
    errores = []

    # Пример проверки
    if datos.get('dolor') == 'Нет' and datos.get('dinamica_hromota') == 'Присутствует':
        errores.append("Вы указали 'Нет боли' на статическом осмотре, но выявили 'Хромоту' в динамическом осмотре.")

    if datos.get('movilidad') == 'Полная' and datos.get('deformacion') == 'Выраженная':
        errores.append("Вы указали 'Полную подвижность', но выбрали 'Выраженную деформацию'. Проверьте данные.")

    if datos.get('temperatura') == 'Повышенная' and datos.get('dolor') == 'Нет':
        errores.append("Повышенная температура кожи указывает на воспаление, но боль не указана. Проверьте данные.")
    
    return errores
