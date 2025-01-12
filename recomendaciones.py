def generar_recomendaciones(datos):
    """
    Генерация рекомендаций по лечению и реабилитации.
    """
    recomendaciones = []

    # Пример логики для генерации рекомендаций
    if datos.get('dolor') == 'Сильная':
        recomendaciones.append("Лазерная терапия: 3-4 раза в неделю для снятия боли.")

    if datos.get('movilidad') == 'Ограниченная':
        recomendaciones.append("Укрепляющие упражнения: 2-3 раза в неделю для восстановления подвижности.")

    if datos.get('ugol_norberg') == '<90°':
        recomendaciones.append("Рекомендуется рентген для оценки состояния тазобедренного сустава.")

    if not recomendaciones:
        recomendaciones.append("Дополнительных рекомендаций не требуется.")
    
    return recomendaciones
